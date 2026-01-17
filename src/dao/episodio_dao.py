from typing import List, Optional
from src.db.dados import get_connection
from src.models.episodio import Episodio


class EpisodioDAO:
    """
    Data Access Object estático completo para a tabela 'episodios'.
    Implementa Create, Read (por ID e por temporada_id), Update e Delete.
    O cadastro de um episódio é obrigatoriamente vinculado a uma temporada_id.
    """

    @staticmethod
    def _mapear_linha_para_objeto(row) -> Optional[Episodio]:
        """Mapeia uma linha do banco para um objeto Episodio."""
        if not row:
            return None

        episodio = Episodio(
            titulo=row["titulo"],
            numero=row["numero"],
            duracao=row["duracao"],
            id=row["id"],
        )
        return episodio

    # --- CREATE ---
    @staticmethod
    def salvar(episodio: Episodio, temporada_id: int) -> int:
        """
        Salva um episódio no banco de dados vinculado a uma temporada.
        """
        if not temporada_id or temporada_id <= 0:
            raise ValueError(
                "temporada_id é obrigatório e deve ser um inteiro positivo."
            )

        sql = "INSERT INTO episodios (temporada_id, numero, titulo, duracao) VALUES (?, ?, ?, ?)"
        params = (temporada_id, episodio.numero, episodio.titulo, episodio.duracao)

        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)

            novo_id = cursor.lastrowid
            episodio.id = novo_id

            conn.commit()
            return novo_id
        finally:
            conn.close()

    # --- READ (Get By ID) ---
    @staticmethod
    def buscar_por_id(id: int) -> Optional[Episodio]:
        """
        Recupera um episódio específico pelo seu identificador único.
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM episodios WHERE id = ?", (id,))
            row = cursor.fetchone()
            return EpisodioDAO._mapear_linha_para_objeto(row)
        finally:
            conn.close()

    # --- READ (Buscar por temporada_id) ---
    @staticmethod
    def buscar_por_temporada_id(temporada_id: int) -> List[Episodio]:
        """
        Busca todos os episódios de uma temporada.
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM episodios WHERE temporada_id = ? ORDER BY numero",
                (temporada_id,),
            )
            rows = cursor.fetchall()
            return [EpisodioDAO._mapear_linha_para_objeto(r) for r in rows if r]
        finally:
            conn.close()

    @staticmethod
    def listar_todos() -> List[Episodio]:
        """Retorna todos os episódios."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM episodios ORDER BY temporada_id, numero")
            rows = cursor.fetchall()
            return [EpisodioDAO._mapear_linha_para_objeto(r) for r in rows if r]
        finally:
            conn.close()

    # --- UPDATE ---
    @staticmethod
    def atualizar(episodio: Episodio, temporada_id: int) -> bool:
        """
        Sincroniza as alterações do objeto com o banco de dados.
        """
        if not episodio.id:
            return False

        sql = """
            UPDATE episodios 
            SET temporada_id = ?, numero = ?, titulo = ?, duracao = ?
            WHERE id = ?
        """
        params = (
            temporada_id,
            episodio.numero,
            episodio.titulo,
            episodio.duracao,
            episodio.id,
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
        """Remove permanentemente o episódio do banco."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM episodios WHERE id = ?", (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    @staticmethod
    def buscar_por_midia_id(midia_id: int) -> List[Episodio]:
        """Busca episódios atravessando a tabela de temporadas."""
        sql = """
            SELECT e.* FROM episodios e
            JOIN temporadas t ON e.temporada_id = t.id
            WHERE t.midia_id = ?
            ORDER BY t.numero, e.numero
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (midia_id,))
            rows = cursor.fetchall()
            return [
                Episodio(
                    id=r["id"], 
                    numero=r["numero"], 
                    titulo=r["titulo"], 
                    duracao=r["duracao"]
                ) for r in rows if r
            ]
        finally:
            conn.close()