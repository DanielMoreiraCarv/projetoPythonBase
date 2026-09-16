from datetime import datetime

from app.model.dto.produtoUpdateRequest import ProdutoUpdateRequest
from app.model.produto import Produto
from app.model.dto.produtoCreateRequest import ProdutoCreateRequest
from app.repository.produtoRepository import ProdutoRepository
from app.repository.auditoriaRepository import AuditoriaRepository
from app.model.auditoria import Auditoria

class ProdutoService:
    def __init__(self, produto_repository: ProdutoRepository, auditoria_repository: AuditoriaRepository):
        self.produto_repository = produto_repository
        self.auditoria_repository = auditoria_repository

    def listar(self):
        return self.produto_repository.find_all()

    def criar(self, request: ProdutoCreateRequest):

        produto = Produto(
            descricao=request.descricao,
            marca=request.marca
        )

        produto = self.produto_repository.save(produto)

        auditoria = Auditoria(
            tabela="produtos",
            registro_id=produto.id,
            operacao="CREATE",
            data_operacao=datetime.now()
        )

        self.auditoria_repository.save(auditoria)

        return produto

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
        produto.marca = request.marca
        produto.data_atualizacao = datetime.now()

        produto_atualizado = self.produto_repository.update(produto)

        auditoria = Auditoria(
            tabela="produtos",
            registro_id=produto.id,
            operacao="UPDATE",
            data_operacao=datetime.now()
        )

        self.auditoria_repository.save(auditoria)

        return produto_atualizado


    def deletar(self, produto_id: int):
        produto = self.produto_repository.find_by_id(produto_id)

        if produto is None:
            raise ValueError("Produto não encontrado")

        if produto.data_delecao is not None:
            raise ValueError("Produto já foi deletado")

        produto.data_delecao = datetime.now()

        produto_deletado = self.produto_repository.update(produto)

        auditoria = Auditoria(
            tabela="produtos",
            registro_id=produto.id,
            operacao="DELETE",
            data_operacao=datetime.now()
        )

        self.auditoria_repository.save(auditoria)

        return produto_deletado

    