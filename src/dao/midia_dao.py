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
        """Retorna todas as mídias com as contagens de temporadas e episódios."""
        sql = """
            SELECT 
                m.*,
                (SELECT COUNT(*) FROM temporadas t WHERE t.midia_id = m.id) as total_temps,
                (SELECT COUNT(*) FROM episodios e 
                 JOIN temporadas t ON e.temporada_id = t.id 
                 WHERE t.midia_id = m.id) as total_eps,
                (SELECT IFNULL(SUM(e.duracao), 0) FROM episodios e 
                 JOIN temporadas t ON e.temporada_id = t.id 
                 WHERE t.midia_id = m.id) as duracao_total_eps
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
