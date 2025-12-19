from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from src.enums.enums import Classificacao, Genero, TipoMidia


class Midia(ABC):
    """
    Representação abstrata de uma mídia para o catálogo.

    Esta classe define a interface e o comportamento comum para todas as mídias,
    garantindo que atributos obrigatórios sejam validados antes da inserção
    no banco de dados SQLite.

    Attributes:
        id (Optional[int]): Identificador único gerado pelo banco de dados.
        titulo (str): Título da mídia.
        tipo (TipoMidia): Categoria da mídia (Filme ou Série).
        genero (Genero): Gênero cinematográfico.
        ano (int): Ano de lançamento.
        classificacao (Classificacao): Classificação indicativa.
        elenco (str): Texto contendo o nome dos atores.
    """

    def __init__(
        self,
        titulo: str,
        tipo: TipoMidia,
        genero: Genero,
        ano: int,
        classificacao: Classificacao,
        elenco: str,
    ):
        self._id: Optional[int] = None

        # Atributos privados tipados
        self._titulo: str
        self._tipo: TipoMidia
        self._genero: Genero
        self._ano: int
        self._classificacao: Classificacao
        self._elenco: str

        # Inicialização com validação via setters
        self.titulo = titulo
        self.tipo = tipo
        self.genero = genero
        self.ano = ano
        self.classificacao = classificacao
        self.elenco = elenco

    # --- PROPRIEDADES (GETTERS E SETTERS) ---

    # ID
    @property
    def id(self) -> Optional[int]:
        """Retorna o ID da mídia ou None se não persistido."""
        return self._id

    @id.setter
    def id(self, valor: int):
        if valor <= 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self._id = valor

    # TITULO
    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O título é obrigatório.")
        self._titulo = valor.strip()

    # TIPO
    @property
    def tipo(self) -> str:
        """Retorna o valor textual do TipoMidia."""
        return self._tipo.value

    @tipo.setter
    def tipo(self, valor: TipoMidia):
        if not isinstance(valor, TipoMidia):
            raise ValueError("O valor deve ser um membro da Enum TipoMidia.")
        self._tipo = valor

    # GENERO
    @property
    def genero(self) -> str:
        """Retorna o valor textual do Gênero."""
        return self._genero.value

    @genero.setter
    def genero(self, valor: Genero):
        if not isinstance(valor, Genero):
            raise ValueError("O valor deve ser um membro da Enum Genero.")
        self._genero = valor

    # ANO
    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, valor: int):
        limite_superior = datetime.now().year + 5
        if not (1888 <= valor <= limite_superior):
            raise ValueError(
                f"Ano inválido. Deve estar entre 1888 e {limite_superior}."
            )
        self._ano = valor

    # CLASSIFICAÇÃO
    @property
    def classificacao(self) -> str:
        """Retorna o valor textual da Classificação."""
        return self._classificacao.value

    @classificacao.setter
    def classificacao(self, valor: Classificacao):
        if not isinstance(valor, Classificacao):
            raise ValueError("O valor deve ser um membro da Enum Classificacao.")
        self._classificacao = valor

    # ELENCO
    @property
    def elenco(self) -> str:
        return self._elenco

    @elenco.setter
    def elenco(self, valor: str):
        """Armazena o elenco como string simples ou vazia se for None."""
        self._elenco = valor.strip() if valor else ""

    # --- MÉTODOS ABSTRATOS ---

    @abstractmethod
    def calcular_media(self) -> float:
        """Calcula a média de notas baseada no RegistroHistorico."""
        pass

    @property
    @abstractmethod
    def duracao(self) -> int:
        """Retorna a duração total da mídia em minutos."""
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Retorna a métrica de tamanho da mídia (minutos ou episódios)."""
        pass

    # --- MÉTODOS ESPECIAIS ---

    def __eq__(self, outra: object) -> bool:
        """Verifica igualdade baseada em título, tipo e ano."""
        if not isinstance(outra, Midia):
            return False
        return (
            self.titulo.lower() == outra.titulo.lower()
            and self.tipo == outra.tipo
            and self.ano == outra.ano
        )

    def __hash__(self) -> int:
        """Gera um hash único para permitir uso em sets e chaves de dict."""
        return hash((self.titulo.lower(), self.tipo, self.ano))

    def __lt__(self, outra: "Midia") -> bool:
        """Permite ordenação padrão por título (ordem alfabética)."""
        if not isinstance(outra, Midia):
            return NotImplemented
        return self.titulo.lower() < outra.titulo.lower()

    def __str__(self) -> str:
        """Formatação amigável para exibição na interface (CLI)."""
        return f"[{self.tipo}] {self.titulo} ({self.ano}) - Gênero: {self.genero}"

    def __repr__(self) -> str:
        """Representação técnica detalhada para depuração e log."""
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, titulo='{self.titulo}', tipo='{self.tipo}', "
            f"genero='{self.genero}', ano={self.ano}, "
            f"classificacao='{self.classificacao}', elenco='{self.elenco}'"
            f")"
        )
