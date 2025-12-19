from typing import List

from models.episodio import Episodio


class Temporada:
    """
    Agrupa episódios, mapeada na tabela 'temporadas'.

    Attributes:
        id (int): Identificador único no banco de dados.
        numero (int): Número da temporada.
    """

    def __init__(self, numero: int, id: int = None):
        """
        Inicializa uma temporada. O ID começa como None por padrão.
        """
        self._id = id
        self._numero = numero
        self._episodios: List[Episodio] = []

    # ID
    @property
    def id(self) -> int:
        """Retorna o ID da temporada."""
        return self._id

    @id.setter
    def id(self, valor: int):
        self._id = valor

    # NUMERO
    @property
    def numero(self) -> int:
        """Retorna o número da temporada."""
        return self._numero

    @numero.setter
    def numero(self, valor: int):
        self._numero = valor

    # EPISODIOS
    @property
    def episodios(self) -> List[Episodio]:
        """Retorna a lista de episódios da temporada."""
        return self._episodios

    # DURAÇÃO TOTAL
    @property
    def duracao_total(self) -> int:
        """Soma das durações de todos os episódios contidos na temporada."""
        return sum(ep.duracao for ep in self._episodios)

    # --- MÉTODOS ---
    def adicionar_episodio(self, episodio: Episodio):
        """
        Adiciona um episódio à lista da temporada.
        """
        if isinstance(episodio, Episodio):
            self._episodios.append(episodio)

    # --- MÉTODOS ESPECIAIS ---
    def __len__(self) -> int:
        return len(self._episodios)

    def __str__(self) -> str:
        return f"Temporada {self._numero} ({len(self)} episódios)"
