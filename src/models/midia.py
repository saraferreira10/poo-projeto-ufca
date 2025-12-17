from abc import ABC, abstractmethod
from datetime import datetime
from src.enums.enums import Classificacao, Genero, StatusVisualizacao, TipoMidia


# --- MIDIA ---
class Midia(ABC):
    # ---  MÉTODO CONSTRUTOR ---
    def __init__(
        self,
        titulo: str,
        tipo: TipoMidia,
        genero: Genero,
        ano: int,
        duracao: int,
        classificacao: Classificacao,
        elenco: str,
    ):
        # DEFINIÇÃO DOS ATRIBUTOS PRIVADOS
        self._id = None
        self._titulo = None
        self._tipo = None
        self._genero = None
        self._ano = None
        self._duracao = None
        self._classificacao = None
        self._elenco = None
        self._status = StatusVisualizacao.NAO_ASSISTIDO
        self._concluido_em = None
        self._nota = 0.0

        # VALIDAÇÃO COM SETTER
        self.titulo = titulo
        self.tipo = tipo
        self.genero = genero
        self.ano = ano
        self.duracao = duracao
        self.classificacao = classificacao
        self.elenco = elenco

    # --- GETTERS E SETTERS ---
    # ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    # TITULO
    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Título não pode ser vazio.")
        self._titulo = valor.strip()

    # TIPO
    @property
    def tipo(self) -> str:
        return self._tipo.value

    @tipo.setter
    def tipo(self, valor: TipoMidia) -> None:
        if not isinstance(valor, TipoMidia):
            raise ValueError("O tipo deve ser um membro da Enum TipoMidia.")
        self._tipo = valor

    # GENERO
    @property
    def genero(self) -> str:
        return self._genero.value

    @genero.setter
    def genero(self, valor: Genero) -> None:
        if not isinstance(valor, Genero):
            raise ValueError("Gênero inválido. Use a Enum Genero.")
        self._genero = valor

    # ANO
    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, valor: int) -> None:
        if not (1888 <= valor <= datetime.now().year + 5):
            raise ValueError("Ano fora do intervalo permitido.")
        self._ano = valor

    # DURAÇÃO
    @property
    def duracao(self) -> int:
        return self._duracao

    @duracao.setter
    def duracao(self, valor: int) -> None:
        if valor <= 0:
            raise ValueError("Duração deve ser positiva.")
        self._duracao = valor

    # CLASSIFICAÇÃO
    @property
    def classificacao(self) -> str:
        return self._classificacao.value

    @classificacao.setter
    def classificacao(self, valor: Classificacao) -> None:
        if not isinstance(valor, Classificacao):
            raise ValueError("Classificação deve ser um membro da Enum Classificacao.")
        self._classificacao = valor

    # ELENCO
    @property
    def elenco(self) -> str:
        return self._elenco

    @elenco.setter
    def elenco(self, valor: str) -> None:
        self._elenco = valor

    # STATUS
    @property
    def status(self) -> str:
        return self._status.value

    # NOTA
    @property
    def nota(self) -> float:
        return self._nota

    # CONCLUÍDO EM
    @property
    def concluido_em(self):
        return self._concluido_em

    # --- MÉTODOS ABSTRATOS ---
    @abstractmethod
    def marcar_assistido(self) -> None:
        pass

    @abstractmethod
    def avaliar(self, nota: float) -> None:
        pass

    @abstractmethod
    def calcular_media(self) -> float:
        pass

    # --- MÉTODOS ESPECIAIS ---
    def __str__(self) -> str:
        return (
            f"--- Detalhes da Mídia ---\n"
            f"Título: {self.titulo}\n"
            f"Tipo: {self.tipo}\n"
            f"Gênero: {self.genero}\n"
            f"Ano: {self.ano}\n"
            f"Duração: {self.duracao} min\n"
            f"Classificação: {self.classificacao}\n"
            f"Elenco: {self.elenco}\n"
            f"Status: {self.status}\n"
            f"Nota: {self.nota:.1f}\n"
            f"------------------------"
        )

    def __repr__(self) -> str:
        return (
            f"Midia(titulo='{self.titulo}', tipo='{self.tipo}', genero='{self.genero}', "
            f"ano={self.ano}, duracao={self.duracao}, classificacao='{self.classificacao}', "
            f"status='{self.status}', nota={self.nota})"
        )

    def __eq__(self, outra: object) -> bool:
        if not isinstance(outra, Midia):
            return False

        return (
            self.titulo.lower() == outra.titulo.lower()
            and self.tipo == outra.tipo
            and self.ano == outra.ano
        )

    def __lt__(self, outra: object) -> bool:
        if not isinstance(outra, Midia):
            return NotImplemented
        return self.nota < outra.nota
