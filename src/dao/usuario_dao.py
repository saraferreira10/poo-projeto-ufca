from typing import List, Optional
from src.db.dados import get_connection
from src.models.usuario import Usuario

class UsuarioDAO:
    """
    Data Access Object para a classe Usuario.
    Gerencia as operações de base de dados para utilizadores sem registo histórico.
    """

    @staticmethod
    def _mapear_linha_para_objeto(row) -> Optional[Usuario]:
        """Converte uma linha da base de dados num objeto Usuario."""
        if not row:
            return None
        
        usuario = Usuario(
            nome=row["nome"],
            email=row["email"]
        )
        usuario.id = row["id"]
        
        return usuario

    @staticmethod
    def salvar(usuario: Usuario) -> int:
        """Guarda um novo utilizador na base de dados."""
        sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"
        params = (usuario.nome, usuario.email) 
        
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            
            novo_id = cursor.lastrowid
            usuario.id = novo_id
            
            conn.commit()
            return novo_id
        finally:
            conn.close()

    @staticmethod
    def buscar_por_id(id: int) -> Optional[Usuario]:
        """Recupera um utilizador pelo seu ID único."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
            row = cursor.fetchone()
            return UsuarioDAO._mapear_linha_para_objeto(row)
        finally:
            conn.close()

    @staticmethod
    def buscar_por_email(email: str) -> Optional[Usuario]:
        """Busca um utilizador pelo e-mail (chave única)."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            row = cursor.fetchone()
            return UsuarioDAO._mapear_linha_para_objeto(row)
        finally:
            conn.close()

    @staticmethod
    def listar_todos() -> List[Usuario]:
        """Retorna uma lista com todos os utilizadores do sistema."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios ORDER BY nome")
            rows = cursor.fetchall()
            return [UsuarioDAO._mapear_linha_para_objeto(r) for r in rows if r]
        finally:
            conn.close()

    @staticmethod
    def deletar(id: int) -> bool:
        """Remove um utilizador da base de dados."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()