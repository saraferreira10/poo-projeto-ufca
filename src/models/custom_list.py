from os import name

from src.models.midia import Midia


class CustomList():
    def __init__(self, name) -> None:
        self._id = None
        self._name = name
        self._media = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Nome da lista não pode ser vazio.")
        self._name = value.strip()

    @property
    def media(self):
        return self._media


    def adicionar(self, media: Midia):
        if media in self._media:
            raise ValueError(f"A mídia '{media.titulo}' já existe na lista personalizada.")
        
        self._media.append(media)
        print(f"Mídia '{media.titulo}' adicionada à lista '{self.name}'")

    #TODO: Criar métodos remover e listar