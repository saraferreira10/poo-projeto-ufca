
import datetime
from typing import List
from src.enums.enums import StatusVisualizacao
from src.models.midia import Midia
from src.models.user import User


class HistoricalRecord():
    def __init__(self, user, media) -> None:
        self._user: User = user
        self._media: Midia = media
        self._progess: int = None
        self._finish: datetime = None
        self._status: StatusVisualizacao = StatusVisualizacao.NAO_ASSISTIDO
        self._rate = None

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User):
        if not isinstance(value, User):
            raise ValueError("O tipo deve ser User.")
        self._user = value

    @property
    def media(self) -> Midia:
        return self._media.copy()

    @property
    def progress(self) -> datetime:
        return self._progress

    @property
    def finish(self) -> datetime:
        return self._finish

    @property
    def status(self) -> StatusVisualizacao:
        return self._status

    @status.setter
    def status(self):
        if self._progess == None:
            self.status = StatusVisualizacao.NAO_ASSISTIDO
        elif self.media._duracao == self._progress:
            self.status = StatusVisualizacao.ASSISTIDO
        else:
            self.status = StatusVisualizacao.ASSISTINDO


    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, valor: int):
        if valor < 0 or valor > 10:
            raise ValueError("Nota deve ser um valor de 0 a 10")

        self._rate = valor
        print(f"Você atribuiu uma nota '{self.rate}' para '{self.midia.titulo}'")


    