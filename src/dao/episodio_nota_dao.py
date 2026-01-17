from src.db.dados import get_connection


class EpisodioNotaDAO:
    """
    Data Access Object para a tabela 'episodio_notas'.
    Gerencia as avaliações individuais de cada episódio.
    """

    @staticmethod
    def salvar(episodio_id: int, usuario_id: int, nota: int) -> bool:
        """
        Registra uma nota para um episódio específico vinculada a um usuário.
        """
        sql = """
            INSERT INTO episodio_notas (episodio_id, usuario_id, nota) 
            VALUES (?, ?, ?)
        """
        params = (episodio_id, usuario_id, nota)

        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao salvar nota do episódio: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def buscar_notas_por_episodio(episodio_id: int):
        """Retorna todas as notas de um episódio específico."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM episodio_notas WHERE episodio_id = ?", (episodio_id,)
            )
            return cursor.fetchall()
        finally:
            conn.close()
    
