class Usuario():
    def __init__(
        self, 
        nome: str, 
        email: str
    ):

        self._id = None
        self._nome = nome
        self._email = email

    # ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # NOME    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    # EMAIL    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value) -> None:
        if not value.strip():
            raise ValueError("E-mail não pode ser vazio")
        self._email = value.strip()

    # REGISTRO HISTÓRICO
