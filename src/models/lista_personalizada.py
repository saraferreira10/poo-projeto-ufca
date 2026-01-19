from src.models.midia import Midia

class ListaPersonalizada():
    def __init__(self, nome) -> None:
        self._id = None
        self._nome = nome
        self._midias = []

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

    @property
    def midias(self):
        return self._midias


    def adicionar(self, midia: Midia):
        if midia in self._midias:
            raise ValueError(f"A mídia '{midia.titulo}' já existe na lista personalizada.")
        
        self._midias.append(midia)
        print(f"Mídia '{midia.titulo}' adicionada à lista '{self.nome}'")

    #TODO: Criar métodos remover e listar