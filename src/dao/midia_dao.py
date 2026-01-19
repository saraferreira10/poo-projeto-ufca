from typing import List, Optional
from src.db.dados import get_connection
from src.models.midia import Midia
from src.models.serie import Serie
from src.models.filme import Filme
from src.enums.enums import TipoMidia, Genero, Classificacao


class MidiaDAO:
    """
    Data Access Object estático completo para a tabela 'midia'.
    Implementa Create, Read (por ID e Filtros), Update e Delete.
    """

    @staticmethod
    def _mapear_linha_para_objeto(row) -> Optional[Midia]:
        if not row:
            return None

        # Recupera o ID do banco
        id_do_banco = row["id"]
        
        params = {
            "titulo": row["titulo"],
            "genero": Genero(row["genero"]),
            "ano": row["ano"],
            "classificacao": Classificacao(row["classificacao"]),
            "elenco": row["elenco"],
        }

        tipo = row["tipo"]
        objeto_midia = None

        if tipo == TipoMidia.FILME.value:
            objeto_midia = Filme(**params, duracao=row["duracao"])
        elif tipo == TipoMidia.SERIE.value:
            objeto_midia = Serie(**params)

        if objeto_midia is not None and id_do_banco is not None:
            try:
                id_int = int(id_do_banco)
                if id_int > 0:
                    objeto_midia.id = id_int
            except (ValueError, TypeError):
                pass

        return objeto_midia

    # --- CREATE ---
    @staticmethod
    def salvar(midia: Midia) -> int:
        sql = "INSERT INTO midia (tipo, titulo, genero, ano, classificacao, elenco, duracao) VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = (
            midia.tipo, 
            midia.titulo,
            midia.genero, 
            midia.ano,
            midia.classificacao, 
            midia.elenco,
            midia.duracao,
        )

        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)

            novo_id = cursor.lastrowid

            midia.id = novo_id

            conn.commit()
            return novo_id
        finally:
            conn.close()

    # --- READ (Get By ID) ---
    @staticmethod
    def buscar_por_id(id: int) -> Optional[Midia]:
        """
        Recupera uma mídia específica pelo seu identificador único.
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM midia WHERE id = ?", (id,))
            row = cursor.fetchone()
            return MidiaDAO._mapear_linha_para_objeto(row)
        finally:
            conn.close()

    # --- READ (Filtros e Listagem) ---
    @staticmethod
    def buscar_por_titulo(titulo: str) -> List[Midia]:
        """
        Busca mídias que contenham parte do título informado.
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM midia WHERE titulo LIKE ?", (f"%{titulo}%",))
            rows = cursor.fetchall()
            return [MidiaDAO._mapear_linha_para_objeto(r) for r in rows if r]
        finally:
            conn.close()

    @staticmethod
    def listar_todos():
        sql = """
            SELECT 
                m.*,
                (SELECT COUNT(*) FROM temporadas t WHERE t.midia_id = m.id) as total_temps,
                (SELECT COUNT(*) FROM episodios e 
                 JOIN temporadas t ON e.temporada_id = t.id 
                 WHERE t.midia_id = m.id) as total_eps,
                (SELECT IFNULL(SUM(e.duracao), 0) FROM episodios e 
                 JOIN temporadas t ON e.temporada_id = t.id 
                 WHERE t.midia_id = m.id) as duracao_total_eps,
                CASE 
                    WHEN m.tipo = 'SERIE' THEN (
                        SELECT IFNULL(AVG(en.nota), 0)
                        FROM episodio_notas en
                        JOIN episodios ep ON en.episodio_id = ep.id
                        JOIN temporadas tp ON ep.temporada_id = tp.id
                        WHERE tp.midia_id = m.id
                    )
                    ELSE (
                        SELECT IFNULL(AVG(nota), 0) 
                        FROM avaliacoes 
                        WHERE midia_id = m.id
                    )
                END as media_nota
            FROM midia m
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conn.close()

    # --- UPDATE ---
    @staticmethod
    def atualizar(midia: Midia) -> bool:
        """Sincroniza as alterações do objeto com o banco de dados."""
        if not midia.id:
            return False

        sql = """
            UPDATE midia 
            SET titulo = ?, genero = ?, ano = ?, classificacao = ?, elenco = ?, duracao = ?
            WHERE id = ?
        """
        params = (
            midia.titulo,
            midia.genero,
            midia.ano,
            midia.classificacao,
            midia.elenco,
            midia.duracao,
            midia.id,
        )

        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    # --- DELETE ---
    @staticmethod
    def deletar(id: int) -> bool:
        """Remove permanentemente a mídia do banco."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM midia WHERE id = ?", (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    @staticmethod
    def buscar_top_10():
        """
        Retorna as 10 mídias mais bem avaliadas.
        Calcula a média de episódios para séries e avaliações diretas para filmes.
        """
        sql = """
            SELECT id, titulo, tipo, 
            CASE 
                WHEN tipo = 'SERIE' THEN (
                    SELECT AVG(en.nota) 
                    FROM episodio_notas en
                    JOIN episodios ep ON en.episodio_id = ep.id
                    JOIN temporadas tp ON ep.temporada_id = tp.id
                    WHERE tp.midia_id = midia.id
                )
                ELSE (
                    SELECT AVG(nota) 
                    FROM avaliacoes 
                    WHERE midia_id = midia.id
                )
            END as media
            FROM midia
            WHERE media IS NOT NULL
            ORDER BY media DESC
            LIMIT 10
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def relatorio_media_por_genero():
        """Média de notas agrupadas por gênero (Filmes e Séries combinados)"""
        sql = """
            SELECT genero, AVG(nota) as media 
            FROM (
                SELECT m.genero, a.nota FROM midia m JOIN avaliacoes a ON m.id = a.midia_id
                UNION ALL
                SELECT m.genero, en.nota FROM midia m 
                JOIN temporadas t ON m.id = t.midia_id
                JOIN episodios e ON t.id = e.temporada_id
                JOIN episodio_notas en ON e.id = en.episodio_id
            )
            GROUP BY genero ORDER BY media DESC
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def relatorio_tempo_por_tipo():
        """Soma da duração de mídias e episódios com status 'ASSISTIDO'"""
        sql = """
            SELECT 'FILME' as tipo, IFNULL(SUM(m.duracao), 0) as total
            FROM midia m
            JOIN visualizacoes_filme vf ON m.id = vf.midia_id
            WHERE vf.status = 'ASSISTIDO'
            UNION ALL
            SELECT 'SERIE' as tipo, IFNULL(SUM(e.duracao), 0) as total
            FROM episodios e
            JOIN visualizacoes_episodio ve ON e.id = ve.episodio_id
            WHERE ve.status = 'ASSISTIDO'
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def relatorio_series_mais_assistidas():
        """Séries com maior contagem de episódios marcados como 'ASSISTIDO'"""
        sql = """
            SELECT m.titulo, COUNT(ve.id) as total_eps
            FROM midia m
            JOIN temporadas t ON m.id = t.midia_id
            JOIN episodios e ON t.id = e.temporada_id
            JOIN visualizacoes_episodio ve ON e.id = ve.episodio_id
            WHERE ve.status = 'ASSISTIDO'
            GROUP BY m.id
            ORDER BY total_eps DESC
            LIMIT 5
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def contar_total_midias():
        """Conta o total de mídias no banco de dados"""
        sql = "SELECT COUNT(*) FROM midia"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()[0]
        finally:
            conn.close()

    @staticmethod
    def contar_total_filmes():
        """Conta o total de filmes no banco de dados"""
        sql = "SELECT COUNT(*) FROM filme"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()[0]
        finally:
            conn.close()

    @staticmethod
    def contar_total_series():
        """Conta o total de séries no banco de dados"""
        sql = "SELECT COUNT(*) FROM serie"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()[0]
        finally:
            conn.close()

    @staticmethod
    def calcular_tempo_total_assistido():
        """Calcula o tempo total assistido de todas as mídias"""
        sql = """
            SELECT SUM(duracao) FROM midia
            JOIN visualizacoes_filme ON midia.id = visualizacoes_filme.midia_id
            WHERE visualizacoes_filme.status = 'ASSISTIDO'
        """
        conn = get_connection()
        if conn is None:
            return 0
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()[0]
        finally:
            conn.close()

    @staticmethod
    def obter_estatisticas_gerais():
        """Retorna um dicionário com estatísticas do catálogo para a tela inicial."""
        sql = """
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN tipo = 'FILME' THEN 1 ELSE 0 END) as filmes,
                SUM(CASE WHEN tipo = 'SERIE' THEN 1 ELSE 0 END) as series,
                IFNULL((
                    SELECT SUM(m.duracao)
                    FROM midia m
                    JOIN visualizacoes_filme vf ON m.id = vf.midia_id
                    WHERE vf.status = 'ASSISTIDO'
                ), 0) + 
                IFNULL((
                    SELECT SUM(e.duracao)
                    FROM episodios e
                    JOIN visualizacoes_episodio ve ON e.id = ve.episodio_id
                    WHERE ve.status = 'ASSISTIDO'
                ), 0) as tempo_total
            FROM midia
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()
            if row:
                return {
                    "total": row["total"] or 0,
                    "filmes": row["filmes"] or 0,
                    "series": row["series"] or 0,
                    "tempo_total": row["tempo_total"] or 0
                }
            return {"total": 0, "filmes": 0, "series": 0, "tempo_total": 0}
        finally:
            conn.close()

