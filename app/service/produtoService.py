import datetime

from app.model.dto.produtoUpdateRequest import ProdutoUpdateRequest
from app.model.produto import Produto
from app.model.dto.produtoCreateRequest import ProdutoCreateRequest
from app.repository.produtoRepository import ProdutoRepository

class ProdutoService:
    def __init__(self, produto_repository: ProdutoRepository):
        self.produto_repository = produto_repository

    def listar(self):
        return self.produto_repository.find_all()

    def criar(self, request: ProdutoCreateRequest):

        produto = Produto(
            descricao=request.descricao,
            marca=request.marca
        )

        return self.produto_repository.save(produto)
    

    def buscar_por_id(self, produto_id: int):
        produto = self.produto_repository.find_by_id(produto_id)

        if produto is None:
            raise ValueError("Produto não encontrado")

        return produto

    def atualizar(
        self,
        produto_id: int,
        request: ProdutoUpdateRequest
    ):
        produto = self.produto_repository.find_by_id(produto_id)

        if produto is None:
            raise ValueError("Produto não encontrado")

        if produto.data_delecao is not None:
            raise ValueError("Produto já foi deletado")

        produto.descricao = request.descricao
        produto.quantidade = request.quantidade
        produto.marca = request.marca
        produto.data_atualizacao = datetime.now()

        return self.produto_repository.update(produto)


    def deletar(self, produto_id: int):
        produto = self.produto_repository.find_by_id(produto_id)

        if produto is None:
            raise ValueError("Produto não encontrado")

        if produto.data_delecao is not None:
            raise ValueError("Produto já foi deletado")

        return self.produto_repository.delete(produto)

    