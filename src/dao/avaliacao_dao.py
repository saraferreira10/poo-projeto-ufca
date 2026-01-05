from typing import Optional
from datetime import datetime
from src.db.dados import get_connection
from src.models.avaliacao import Avaliacao

class AvaliacaoDAO:
    @staticmethod
    def _mapear_linha_avaliacao_para_objeto(row) -> Optional[Avaliacao]:
        if not row: return None
        data_str = row["data_avaliacao"]
        try:
            data_avaliacao = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            data_avaliacao = datetime.now()

        avaliacao = Avaliacao(
            usuario_id=row["usuario_id"],
            midia_id=row["midia_id"],
            nota=row["nota"],
            comentario=row.get("comentario", "") or ""
        )
        avaliacao.id = row["id"]
        avaliacao._data_avaliacao = data_avaliacao
        return avaliacao

    @staticmethod
    def salvar_avaliacao(avaliacao: Avaliacao) -> int:
        sql = "INSERT INTO avaliacoes (usuario_id, midia_id, nota, comentario, data_avaliacao) VALUES (?, ?, ?, ?, ?)"
        params = (avaliacao.usuario_id, avaliacao.midia_id, avaliacao.nota, 
                  avaliacao.comentario, avaliacao._data_avaliacao.strftime("%Y-%m-%d %H:%M:%S"))
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            novo_id = cursor.lastrowid
            avaliacao.id = novo_id
            conn.commit()
            return novo_id
        finally:
            conn.close()

    @staticmethod
    def calcular_media_avaliacoes_midia(midia_id: int) -> float:
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT AVG(nota) as media FROM avaliacoes WHERE midia_id = ?", (midia_id,))
            row = cursor.fetchone()
            return float(row["media"]) if row and row["media"] is not None else 0.0
        finally:
            conn.close()