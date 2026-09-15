from datetime import datetime
from pydantic import BaseModel

class AuxProdutoEstoqueResponse(BaseModel):
    id: int
    id_estoque: int
    id_produto: int
    quantidade: int