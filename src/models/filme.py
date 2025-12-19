from src.models.midia import Midia
from src.enums.enums import TipoMidia, Genero, Classificacao


class Filme(Midia):
    """
    Representa uma mídia do tipo Filme no sistema.

    Diferente das séries, o filme possui uma duração fixa em minutos
    armazenada diretamente no banco de dados.

    Attributes:
        titulo (str): Título do filme.
        genero (Genero): Gênero do filme.
        ano (int): Ano de lançamento.
        duracao (int): Duração total em minutos.
        classificacao (Classificacao): Classificação indicativa.
        elenco (str): String simples com o nome dos atores.
    """

    def __init__(
        self,
        titulo: str,
        genero: Genero,
        ano: int,
        duracao: int,
        classificacao: Classificacao,
        elenco: str,
    ):
        self._duracao_fixa = duracao
        super().__init__(titulo, TipoMidia.FILME, genero, ano, classificacao, elenco)

    # --- IMPLEMENTAÇÃO DOS MÉTODOS ABSTRATOS ---

    @property
    def duracao(self) -> int:
        """Retorna a duração fixa do filme (em minutos)."""
        return self._duracao_fixa

    @duracao.setter
    def duracao(self, valor: int):
        if valor <= 0:
            raise ValueError(
                "A duração do filme deve ser um valor positivo em minutos."
            )
        self._duracao_fixa = valor

    def calcular_media(self) -> float:
        """
        Calcula a média de avaliações do filme.
        """
        # TODO: implementar lógica de cálculo da média a partir 
        return 0.0

    def __len__(self) -> int:
        """
        Para Filmes, o tamanho da mídia é representada pela sua duração em minutos.
        """
        return self.duracao