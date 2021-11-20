from typing_extensions import TypedDict
from config import PgLogin


class UserType(TypedDict):
    email: str
    senha: str
    nome: str
    sobrenome: str

class IdUserResponse(TypedDict):
    iduser: int


class Users():
    def __init__(self):
        self.db = PgLogin()

    def insert(self, data: UserType) -> IdUserResponse():
        query = f"""
            insert into tbusers (nome, sobrenome, email, senha) 
            values (
                '{data['nome']}', 
                '{data['sobrenome']}', 
                '{data['email']}', 
                '{data['senha']}'
            ) returning iduser;"""
        
        idUser = self.db.select(query)
        return idUser[0]
