from pydantic import BaseModel

class AuxProdutoEstoqueCreateRequest(BaseModel):
    id_estoque: int
    id_produto: int
    quantidade: int