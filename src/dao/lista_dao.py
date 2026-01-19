from typing import List, Optional
from src.db.dados import get_connection


class ListaDAO:
    """
    Data Access Object para gerenciar listas personalizadas.
    """

    @staticmethod
    def criar_lista(usuario_id: int, nome: str) -> Optional[int]:
        """Cria uma nova lista personalizada para o usuário."""
        sql = "INSERT INTO listas_personalizadas (usuario_id, nome) VALUES (?, ?)"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (usuario_id, nome))
            novo_id = cursor.lastrowid
            conn.commit()
            return novo_id
        except Exception as e:
            print(f"Erro ao criar lista: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def buscar_por_nome(usuario_id: int, nome: str) -> Optional[dict]:
        """Busca uma lista pelo nome do usuário."""
        sql = "SELECT * FROM listas_personalizadas WHERE usuario_id = ? AND nome = ?"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (usuario_id, nome))
            row = cursor.fetchone()
            if row:
                return {"id": row["id"], "usuario_id": row["usuario_id"], "nome": row["nome"]}
            return None
        finally:
            conn.close()

    @staticmethod
    def listar_por_usuario(usuario_id: int) -> List[dict]:
        """Lista todas as listas de um usuário."""
        sql = "SELECT * FROM listas_personalizadas WHERE usuario_id = ? ORDER BY nome"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (usuario_id,))
            rows = cursor.fetchall()
            return [{"id": r["id"], "nome": r["nome"]} for r in rows]
        finally:
            conn.close()

    @staticmethod
    def adicionar_midia(lista_id: int, midia_id: int) -> bool:
        """Adiciona uma mídia a uma lista."""
        sql = "INSERT OR IGNORE INTO itens_lista (lista_id, midia_id) VALUES (?, ?)"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (lista_id, midia_id))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao adicionar mídia à lista: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def remover_midia(lista_id: int, midia_id: int) -> bool:
        """Remove uma mídia de uma lista."""
        sql = "DELETE FROM itens_lista WHERE lista_id = ? AND midia_id = ?"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (lista_id, midia_id))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    @staticmethod
    def listar_midias(lista_id: int) -> List[dict]:
        """Lista todas as mídias de uma lista."""
        sql = """
            SELECT m.* FROM midia m
            JOIN itens_lista il ON m.id = il.midia_id
            WHERE il.lista_id = ?
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (lista_id,))
            return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def deletar_lista(lista_id: int) -> bool:
        """Remove uma lista personalizada."""
        sql = "DELETE FROM listas_personalizadas WHERE id = ?"
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (lista_id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()
