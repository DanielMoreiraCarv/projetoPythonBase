from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class RegistroMovimentacaoUpdateRequest(BaseModel):
    id_estoque_chegada: int | None = None
    id_estoque_saida: int | None = None
    id_produto: int
    quantidade:int
    dsc_responsavel: str
    tip_movimentacao: Literal[0,1,2]
    data_movimentacao: datetime | None = None