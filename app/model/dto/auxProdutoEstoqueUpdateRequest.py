from pydantic import BaseModel

class AuxProdutoEstoqueUpdateRequest(BaseModel):
    id_estoque: int
    id_produto: int
    quantidade: int