
import datetime
from typing import List
from src.enums.enums import StatusVisualizacao
from src.models.midia import Midia
from src.models.usuario import Usuario


class RegistroHistorico():
    def __init__(self, usuario, midia) -> None:
        self._usuario: Usuario = usuario
        self._midia: Midia = midia
        self._progresso: int = None
        self._conclusao: datetime = None
        self._status: StatusVisualizacao = StatusVisualizacao.NAO_ASSISTIDO
        self._nota = None

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @usuario.setter
    def usuario(self, value: Usuario):
        if not isinstance(value, Usuario):
            raise ValueError("O tipo deve ser Usuario.")
        self._usuario = value

    @property
    def midia(self) -> Midia:
        return self._midia

    @property
    def progresso(self) -> datetime:
        return self._progresso

    @property
    def conclusao(self) -> datetime:
        return self._conclusao

    @property
    def status(self) -> StatusVisualizacao:
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor: int):
        if valor < 0 or valor > 10:
            raise ValueError("Nota deve ser um valor de 0 a 10")

        self._nota = valor
        print(f"Você atribuiu uma nota '{self.nota}' para '{self.midia.titulo}'")


    