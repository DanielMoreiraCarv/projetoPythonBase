from datetime import datetime
from pydantic import BaseModel
from typing import Literal

class RegistroMovimentacaoResponse(BaseModel):
    id: int
    id_estoque_chegada: int | None
    id_estoque_saida: int | None
    id_produto: int
    quantidade: int 
    data_movimentacao: datetime | None
    dsc_responsavel: str | None
    tip_movimentacao: Literal[0, 1, 2] 

    class Config:
        from_attributes = True