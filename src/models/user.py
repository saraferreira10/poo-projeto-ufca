from src.models.historical_record import HistoricalRecord

# --- USUÁRIO ---
class User():
    def __init__(
        self, 
        name: str, 
        email: str, 
        historical_record: HistoricalRecord
    ):

        self._id = None
        self._name = name
        self._email = email
        self._custom_list = []
       #self._historical_record = historical_record

    # ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # NAME    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # EMAIL    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value) -> None:
        if not value.strip():
            raise ValueError("E-mail não pode ser vazio")
        self._email = value.strip()

    # CUSTOM_LIST    
    @property
    def custom_list(self):
        return self._custom_list
 
    # HISTORICAL RECORD

    