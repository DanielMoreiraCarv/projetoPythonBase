from pydantic import BaseModel


class ProdutoUpdateRequest(BaseModel):
    descricao: str
    marca: str