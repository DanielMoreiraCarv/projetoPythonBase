from pydantic import BaseModel

class ProdutoCreateRequest(BaseModel):
    marca: str
    descricao: str