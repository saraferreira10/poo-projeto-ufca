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

    @staticmethod
    def listar_historico_episodios(usuario_id: int):
        """Retorna o histórico de episódios visualizados pelo usuário."""
        sql = """
            SELECT m.titulo as serie_titulo, e.numero, e.titulo as ep_titulo, ve.status
            FROM visualizacoes_episodio ve
            JOIN episodios e ON ve.episodio_id = e.id
            JOIN temporadas t ON e.temporada_id = t.id
            JOIN midia m ON t.midia_id = m.id
            WHERE ve.usuario_id = ?
            ORDER BY m.titulo, e.numero
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (usuario_id,))
            return cursor.fetchall()
        finally:
            conn.close()