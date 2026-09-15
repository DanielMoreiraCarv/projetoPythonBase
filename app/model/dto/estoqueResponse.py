from datetime import datetime
from pydantic import BaseModel

class EstoqueResponse(BaseModel):
    id: int
    cep: str
    numero_local: int
    telefone: str
    data_atualizacao: datetime | None
    data_criacao: datetime | None
    data_delecao: datetime | None

    class Config:
        from_attributes = True