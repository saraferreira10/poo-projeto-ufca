from src.db.dados import get_connection

class VisualizacaoDAO:
    @staticmethod
    def atualizar_status(episodio_id: int, usuario_id: int, status: str):
        """
        Insere ou atualiza o status de visualização de um episódio.
        Status comuns: 'ASSISTIDO', 'PENDENTE'
        """
        sql = """
            INSERT OR REPLACE INTO visualizacoes_episodio (episodio_id, usuario_id, status)
            VALUES (?, ?, ?)
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (episodio_id, usuario_id, status.upper()))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao salvar visualização: {e}")
            return False
        finally:
            conn.close()