from pydantic import BaseModel

class EstoqueCreateRequest(BaseModel):
    cep: str
    numero_local: int
    telefone: str