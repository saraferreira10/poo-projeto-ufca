class ListaPersonalizada():
    def __init__(self, nome) -> None:
        self._id = None
        self._nome = nome

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not value.strip():
            raise ValueError("Nome da lista não pode ser vazio.")
        self._nome = value.strip()
