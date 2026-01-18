"""
Script para popular o banco de dados com dados de exemplo.
Executar na raiz do projeto: python3 -m src.db.seed
"""
from src.dao.midia_dao import MidiaDAO
from src.dao.temporada_dao import TemporadaDAO
from src.dao.episodio_dao import EpisodioDAO
from src.models.filme import Filme
from src.models.serie import Serie
from src.models.temporada import Temporada
from src.models.episodio import Episodio
from src.enums.enums import Genero, Classificacao


def popular_banco():
    """Popula o banco de dados com 3 filmes e 3 séries de exemplo."""
    print("🌱 Semeando banco de dados...")

    # ==================== FILMES ====================
    filmes = [
        Filme(
            titulo="Inception",
            genero=Genero.FICCAO_CIENTIFICA,
            ano=2010,
            duracao=148,
            classificacao=Classificacao.C14,
            elenco="Leonardo DiCaprio, Marion Cotillard, Tom Hardy"
        ),
        Filme(
            titulo="O Poderoso Chefão",
            genero=Genero.DRAMA,
            ano=1972,
            duracao=175,
            classificacao=Classificacao.C16,
            elenco="Marlon Brando, Al Pacino, James Caan"
        ),
        Filme(
            titulo="Matrix",
            genero=Genero.FICCAO_CIENTIFICA,
            ano=1999,
            duracao=136,
            classificacao=Classificacao.C14,
            elenco="Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss"
        )
    ]

    print("\n📽️  Adicionando filmes...")
    for filme in filmes:
        try:
            MidiaDAO.salvar(filme)
            print(f"  ✅ {filme.titulo} adicionado")
        except Exception as e:
            print(f"  ⚠️  {filme.titulo}: {e}")

    # ==================== SÉRIES ====================
    series = [
        Serie(
            titulo="Breaking Bad",
            genero=Genero.DRAMA,
            ano=2008,
            classificacao=Classificacao.C16,
            elenco="Bryan Cranston, Aaron Paul, Anna Gunn"
        ),
        Serie(
            titulo="Stranger Things",
            genero=Genero.FICCAO_CIENTIFICA,
            ano=2016,
            classificacao=Classificacao.C14,
            elenco="Millie Bobby Brown, Finn Wolfhard, David Harbour"
        ),
        Serie(
            titulo="The Office",
            genero=Genero.COMEDIA,
            ano=2005,
            classificacao=Classificacao.C12,
            elenco="Steve Carell, John Krasinski, Jenna Fischer"
        )
    ]

    print("\n📺 Adicionando séries...")
    for serie in series:
        try:
            MidiaDAO.salvar(serie)
            print(f"  ✅ {serie.titulo} adicionada")
            
            # Adicionar temporadas e episódios para cada série
            if serie.titulo == "Breaking Bad":
                # Temporada 1 - 7 episódios
                temp1 = Temporada(numero=1)
                TemporadaDAO.salvar(temp1, serie.id)
                episodios_temp1 = [
                    Episodio(titulo="Pilot", numero=1, duracao=58),
                    Episodio(titulo="Cat's in the Bag...", numero=2, duracao=48),
                    Episodio(titulo="...And the Bag's in the River", numero=3, duracao=48),
                    Episodio(titulo="Cancer Man", numero=4, duracao=48),
                    Episodio(titulo="Gray Matter", numero=5, duracao=48),
                    Episodio(titulo="Crazy Handful of Nothin'", numero=6, duracao=48),
                    Episodio(titulo="A No-Rough-Stuff-Type Deal", numero=7, duracao=48)
                ]
                for ep in episodios_temp1:
                    EpisodioDAO.salvar(ep, temp1.id)
                
            elif serie.titulo == "Stranger Things":
                # Temporada 1 - 8 episódios
                temp1 = Temporada(numero=1)
                TemporadaDAO.salvar(temp1, serie.id)
                episodios_temp1 = [
                    Episodio(titulo="Chapter One: The Vanishing of Will Byers", numero=1, duracao=48),
                    Episodio(titulo="Chapter Two: The Weirdo on Maple Street", numero=2, duracao=55),
                    Episodio(titulo="Chapter Three: Holly, Jolly", numero=3, duracao=51),
                    Episodio(titulo="Chapter Four: The Body", numero=4, duracao=50),
                    Episodio(titulo="Chapter Five: The Flea and the Acrobat", numero=5, duracao=52),
                    Episodio(titulo="Chapter Six: The Monster", numero=6, duracao=47),
                    Episodio(titulo="Chapter Seven: The Bathtub", numero=7, duracao=42),
                    Episodio(titulo="Chapter Eight: The Upside Down", numero=8, duracao=55)
                ]
                for ep in episodios_temp1:
                    EpisodioDAO.salvar(ep, temp1.id)
                    
            elif serie.titulo == "The Office":
                # Temporada 1 - 6 episódios
                temp1 = Temporada(numero=1)
                TemporadaDAO.salvar(temp1, serie.id)
                episodios_temp1 = [
                    Episodio(titulo="Pilot", numero=1, duracao=22),
                    Episodio(titulo="Diversity Day", numero=2, duracao=22),
                    Episodio(titulo="Health Care", numero=3, duracao=22),
                    Episodio(titulo="The Alliance", numero=4, duracao=22),
                    Episodio(titulo="Basketball", numero=5, duracao=22),
                    Episodio(titulo="Hot Girl", numero=6, duracao=22)
                ]
                for ep in episodios_temp1:
                    EpisodioDAO.salvar(ep, temp1.id)
                    
        except Exception as e:
            print(f"  ⚠️  {serie.titulo}: {e}")

    print("\n✅ Banco de dados populado com sucesso!")
    print(f"   📽️  {len(filmes)} filmes")
    print(f"   📺 {len(series)} séries")


if __name__ == "__main__":
    from src.db.dados import criar_tabelas
    criar_tabelas()
    popular_banco()
