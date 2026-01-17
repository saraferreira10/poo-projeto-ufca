from src.db.dados import get_connection
from datetime import datetime

class VisualizacaoFilmeDAO:
    @staticmethod
    def atualizar_status(midia_id: int, usuario_id: int, status: str):
        """
        Status permitidos: 'NÃO ASSISTIDO', 'ASSISTINDO', 'ASSISTIDO'
        """
        status = status.upper()
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sql = """
            INSERT OR REPLACE INTO visualizacoes_filme (midia_id, usuario_id, status, data_visualizacao)
            VALUES (?, ?, ?, ?)
        """
        
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (midia_id, usuario_id, status, data_atual))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao salvar visualização do filme: {e}")
            return False
        finally:
            conn.close()