from enum import Enum

class TipoMidia(Enum):
    FILME = "FILME"
    SERIE = "SERIE"

class StatusVisualizacao(Enum):
    NAO_ASSISTIDO = "NÃO ASSISTIDO"
    ASSISTINDO = "ASSISTINDO"
    ASSISTIDO = "ASSISTIDO"

class Classificacao(Enum):
    L   = "L"
    C10 = "10"
    C12 = "12"
    C14 = "14"
    C16 = "16"
    C18 = "18"

class Genero(Enum):
    ACAO = "Ação"
    AVENTURA = "Aventura"
    COMEDIA = "Comédia"
    DRAMA = "Drama"
    FICCAO_CIENTIFICA = "Ficção Científica"
    TERROR = "Terror"
    SUSPENSE = "Suspense"
    ROMANCE = "Romance"
    FANTASIA = "Fantasia"
    DOCUMENTARIO = "Documentário"
    ANIMACAO = "Animação"
    GUERRA = "Guerra"
    HISTORICO = "Histórico"
    POLICIAL = "Policial"
