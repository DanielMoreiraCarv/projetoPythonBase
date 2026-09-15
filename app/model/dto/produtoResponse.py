from datetime import datetime

from pydantic import BaseModel

class ProdutoResponse(BaseModel):
    id: int
    marca: str
    descricao: str
    data_atualizacao: datetime | None
    data_criacao: datetime | None
    data_delecao: datetime | None

    class Config:
        from_attributes = True