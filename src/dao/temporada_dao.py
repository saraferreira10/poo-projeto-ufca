from typing import List, Optional
from src.db.dados import get_connection
from src.models.temporada import Temporada


class TemporadaDAO:
    """
    Data Access Object estático completo para a tabela 'temporadas'.
    Implementa Create, Read (por ID e por midia_id), Update e Delete.
    """

    @staticmethod
    def _mapear_linha_para_objeto(row) -> Optional[Temporada]:
        """Mapeia uma linha do banco para um objeto Temporada."""
        if not row:
            return None

        temporada = Temporada(numero=row["numero"], id=row["id"])
        return temporada

    # --- CREATE ---
    @staticmethod
    def salvar(temporada: Temporada, midia_id: int) -> int:
        """
        Salva uma temporada no banco de dados vinculada a uma mídia.
        """
        sql = "INSERT INTO temporadas (midia_id, numero) VALUES (?, ?)"
        params = (midia_id, temporada.numero)

        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)

            novo_id = cursor.lastrowid
            temporada.id = novo_id

            conn.commit()
            return novo_id
        finally:
            conn.close()

    # --- READ (Get By ID) ---
    @staticmethod
    def buscar_por_id(id: int) -> Optional[Temporada]:
        """
        Recupera uma temporada específica pelo seu identificador único.
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM temporadas WHERE id = ?", (id,))
            row = cursor.fetchone()
            return TemporadaDAO._mapear_linha_para_objeto(row)
        finally:
            conn.close()

    # --- READ (Buscar por midia_id) ---
    @staticmethod
    def buscar_por_midia_id(midia_id: int) -> List[Temporada]:
        """
        Busca todas as temporadas de uma mídia (série).
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM temporadas WHERE midia_id = ? ORDER BY numero",
                (midia_id,)
            )
            rows = cursor.fetchall()
            return [
                TemporadaDAO._mapear_linha_para_objeto(r) for r in rows if r
            ]
        finally:
            conn.close()

    @staticmethod
    def listar_todos() -> List[Temporada]:
        """Retorna todas as temporadas."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM temporadas ORDER BY midia_id, numero")
            rows = cursor.fetchall()
            return [
                TemporadaDAO._mapear_linha_para_objeto(r) for r in rows if r
            ]
        finally:
            conn.close()

    # --- UPDATE ---
    @staticmethod
    def atualizar(temporada: Temporada, midia_id: int) -> bool:
        """Sincroniza as alterações do objeto com o banco de dados."""
        if not temporada.id:
            return False

        sql = """
            UPDATE temporadas 
            SET midia_id = ?, numero = ?
            WHERE id = ?
        """
        params = (midia_id, temporada.numero, temporada.id)

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
        """Remove permanentemente a temporada do banco."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM temporadas WHERE id = ?", (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()
