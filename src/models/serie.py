from typing import List
from src.models.midia import Midia
from src.models.temporada import Temporada
from src.enums.enums import TipoMidia, Genero, Classificacao


class Serie(Midia):
    """
    Representa uma série no sistema, herdando de Midia e mapeada na tabela 'midia'.
    """

    def __init__(
        self,
        titulo: str,
        genero: Genero,
        ano: int,
        classificacao: Classificacao,
        elenco: str,
    ):
        super().__init__(
            titulo, TipoMidia.SERIE, genero, ano, classificacao, elenco
        )
        self._temporadas: List[Temporada] = []


    # TEMPORADAS
    @property
    def temporadas(self) -> List[Temporada]:
        """Retorna a lista de temporadas da série."""
        return self._temporadas

    def adicionar_temporada(self, temporada: Temporada):
        """Adiciona uma temporada à estrutura da série."""
        if isinstance(temporada, Temporada):
            self._temporadas.append(temporada)

    # --- IMPLEMENTAÇÃO DOS MÉTODOS ABSTRATOS DE MIDIA ---
    @property
    def duracao(self) -> int:
        """
        Retorna a duração total da série em minutos.
        Calculada somando a duração de todas as temporadas.
        """
        return sum(t.duracao_total for t in self._temporadas)

    def calcular_media(self) -> float:
        """
        Calcula a média das notas da série.
        """
        # TODO: implementar cálculo de média da série com base em avaliacoes.
        return 0.0

    def __len__(self) -> int:
        """
        Retorna o tamanho da série (total de episódios).
        """
        return sum(len(t) for t in self._temporadas)

    # --- MÉTODOS ESPECIAIS ---
    def __str__(self) -> str:
        return (
            f"[SÉRIE] {self.titulo} ({self.ano}) - "
            f"Gênero: {self.genero} | " 
            f"{len(self._temporadas)} Temps | {len(self)} Eps | "
            f"{self.duracao} min"
        )