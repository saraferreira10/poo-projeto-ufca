from datetime import datetime
from typing import Optional


class Avaliacao:
    """
    Representa a avaliação de uma mídia por um usuário.

    Mapeada na tabela 'avaliacoes' do banco de dados.

    Attributes:
        id (Optional[int]): Identificador único no banco. Nulo se ainda não salvo.
        usuario_id (int): Chave estrangeira referenciando o usuário.
        midia_id (int): Chave estrangeira referenciando a mídia (Filme ou Série).
        nota (int): Valor numérico da avaliação entre 0 e 10.
        comentario (str): Texto opcional com as impressões do usuário.
        data_avaliacao (datetime): Objeto de data e hora da criação.
    """

    def __init__(
        self, usuario_id: int, midia_id: int, nota: int, comentario: str = ""
    ):  # Atributos privados
        self._id: Optional[int] = None
        self._usuario_id: int
        self._midia_id: int
        self._nota: int
        self._comentario: str
        self._data_avaliacao: datetime = datetime.now()

        self.usuario_id = usuario_id
        self.midia_id = midia_id
        self.nota = nota
        self.comentario = comentario

    # ID
    @property
    def id(self) -> Optional[int]:
        """Retorna o ID gerado pelo banco de dados."""
        return self._id

    @id.setter
    def id(self, valor: int):
        self._id = valor

    # USUARIO_ID
    @property
    def usuario_id(self) -> int:
        """ID do autor da avaliação (FK)."""
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, valor: int):
        if valor <= 0:
            raise ValueError("O ID do usuário deve ser um inteiro positivo.")
        self._usuario_id = valor

    # MIDIA_ID
    @property
    def midia_id(self) -> int:
        """ID da mídia associada (FK)."""
        return self._midia_id

    @midia_id.setter
    def midia_id(self, valor: int):
        if valor <= 0:
            raise ValueError("O ID da mídia deve ser um inteiro positivo.")
        self._midia_id = valor

    # NOTA
    @property
    def nota(self) -> int:
        """Nota da avaliação (0 a 10)."""
        return self._nota

    @nota.setter
    def nota(self, valor: int):
        """
        Define a nota com validação de intervalo.
        """
        if not isinstance(valor, int):
            raise ValueError("A nota precisa ser um número inteiro.")
        if not (0 <= valor <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota = valor

    # COMENTÁRIO
    @property
    def comentario(self) -> str:
        """Comentário textual"""
        return self._comentario

    @comentario.setter
    def comentario(self, valor: str):
        self._comentario = valor.strip() if valor else ""

    # DATA AVALIAÇÃO
    @property
    def data_avaliacao(self) -> str:
        """
        Data formatada para exibição (dd/mm/aaaa hh:mm).
        """
        return self._data_avaliacao.strftime("%d/%m/%Y %H:%M")

    # --- MÉTODOS ESPECIAIS ---
    def __repr__(self) -> str:
        """Representação técnica."""
        return (
            f"Avaliacao(id={self.id}, user_id={self.usuario_id}, "
            f"midia_id={self.midia_id}, nota={self.nota})"
        )

    def __str__(self) -> str:
        """Representação para a interface do usuário."""
        estrelas = "★" * (self.nota // 1)
        return f"{estrelas} ({self.nota}/10) - {self.comentario}."
