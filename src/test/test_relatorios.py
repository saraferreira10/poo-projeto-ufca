import pytest
from src.dao.avaliacao_dao import AvaliacaoDAO
from src.dao.midia_dao import MidiaDAO
from src.dao.visualizacao_filme_dao import VisualizacaoFilmeDAO
from src.db.dados import get_connection
from src.models.avaliacao import Avaliacao

def setup_module(module):
    """Limpa e prepara dados de teste no banco"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM avaliacoes")
    cursor.execute("DELETE FROM visualizacoes_filme")
    cursor.execute("DELETE FROM midia")
    
    sql = """
        INSERT INTO midia (id, titulo, tipo, genero, ano, duracao, classificacao) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, (1, 'Filme A', 'FILME', 'Ação', 2024, 120, 'L'))
    cursor.execute(sql, (2, 'Filme B', 'FILME', 'Drama', 2024, 90, '14'))
    
    conn.commit()
    conn.close()

def test_calculo_tempo_total_assistido():
    """Verifica se o relatório de tempo ignora filmes não assistidos"""
    VisualizacaoFilmeDAO.atualizar_status(midia_id=1, usuario_id=1, status='ASSISTIDO')
    VisualizacaoFilmeDAO.atualizar_status(midia_id=2, usuario_id=1, status='ASSISTINDO')

    tempos = MidiaDAO.relatorio_tempo_por_tipo()
    
    total_filme = next(t['total'] for t in tempos if t['tipo'] == 'FILME')
    
    assert total_filme == 120
    assert total_filme != 210

def test_ranking_top_10_ordem():
    """Verifica se o ranking traz a maior nota primeiro"""    
    AvaliacaoDAO.salvar_avaliacao(Avaliacao(usuario_id=1, midia_id=1, nota=10))
    AvaliacaoDAO.salvar_avaliacao(Avaliacao(usuario_id=1, midia_id=2, nota=5))
    
    ranking = MidiaDAO.buscar_top_10()
    
    assert ranking[0]['titulo'] == 'Filme A'
    assert ranking[0]['media'] == 10.0