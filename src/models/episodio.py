class Episodio:
    """
    Representa a unidade básica uma série, mapeada na tabela 'episodios'.

    Attributes:
        id (int): Identificador único no banco de dados.
        titulo (str): Título do episódio.
        numero (int): Ordem do episódio na temporada.
        duracao (int): Duração em minutos.
    """

    def __init__(self, titulo: str, numero: int, duracao: int, id: int = None):
        self._id = id
        self._titulo = titulo.strip()
        self._numero = numero
        self._duracao = duracao

    # ID
    @property
    def id(self) -> int:
        """Retorna o ID do banco de dados."""
        return self._id

    @id.setter
    def id(self, valor: int):
        self._id = valor

    # TITULO
    @property
    def titulo(self) -> str:
        """Retorna o título do episódio."""
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        self._titulo = valor.strip()

    # NUMERO
    @property
    def numero(self) -> int:
        """Retorna o número do episódio."""
        return self._numero

    @numero.setter
    def numero(self, valor: int):
        self._numero = valor

    # DURAÇÃO
    @property
    def duracao(self) -> int:
        """Retorna a duração individual do episódio."""
        return self._duracao

    @duracao.setter
    def duracao(self, valor: int):
        self._duracao = valor

    # --- MÉTODOS ESPECIAIS ---
    def __str__(self) -> str:
        return f"Episódio {self._numero:02d}: {self._titulo} ({self._duracao} min)"