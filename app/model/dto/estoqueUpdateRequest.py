from pydantic import BaseModel

class EstoqueUpdateRequest(BaseModel):
    cep: str
    numero_local: int
    telefone: str
    