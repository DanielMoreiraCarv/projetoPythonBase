from datetime import datetime
from app.model.auditoria import Auditoria
from app.model.dto.auxProdutoEstoqueCreateRequest import AuxProdutoEstoqueCreateRequest
from app.model.dto.auxProdutoEstoqueUpdateRequest import AuxProdutoEstoqueUpdateRequest
from app.model.auxProdutoEstoque import AuxProdutoEstoque
from app.repository.auxProdutoEstoqueRepository import AuxProdutoEstoqueRepository
from app.service.estoqueService import EstoqueService
from app.service.produtoService import ProdutoService
from app.repository.auditoriaRepository import AuditoriaRepository

class AuxProdutoEstoqueService:
    def __init__(self, aux_repository: AuxProdutoEstoqueRepository, prod_service: ProdutoService, est_service: EstoqueService, auditoria_repository: AuditoriaRepository):
        self.aux_repository = aux_repository
        self.prod_service = prod_service
        self.est_service = est_service
        self.auditoria_repository = auditoria_repository

    def listar(self):
        return self.aux_repository.find_all()

    def listar_por_estoque(self, estoque_id: int):
        aux = self.aux_repository.find_by_estoque_id(estoque_id)

        if not aux:
            raise ValueError("Vínculo entre produto e Estoque não encontrado, para o estoque selecionado")

        return aux

    def buscar_aux_por_id(self, id: int):
        aux = self.aux_repository.buscar_por_id(id)

        if aux is None:
            raise ValueError("Vínculo entre produto e Estoque não encontrado")

        return aux

    def buscar_aux(self, id_estoque: int, id_produto: int):
        aux = self.aux_repository.find_by_produto_and_estoque(id_estoque,id_produto)

        if not aux:
            raise ValueError("Vínculo entre produto e Estoque não encontrado")

        return aux

    def criar(self, request: AuxProdutoEstoqueCreateRequest):
        estoque = self.est_service.buscar_por_id(request.id_estoque)

        if estoque is None:
            raise ValueError("Valor de Estoque não encontrado!")

        produto = self.prod_service.buscar_por_id(request.id_produto)

        if produto is None:
            raise ValueError("Valor do Produto não encontrado!")

        aux = AuxProdutoEstoque(
            id_produto = produto.id,
            id_estoque = estoque.id,
            quantidade = request.quantidade
        )

        auxProdutoEstoque = self.aux_repository.save(aux)

        auditoria = Auditoria(
            tabela = "aux_produto_estoque",
            registro_id = auxProdutoEstoque.id,
            operacao = "CREATE",
            data_operacao = datetime.now()
        )

        self.auditoria_repository.save(auditoria)

        return auxProdutoEstoque

    def atualizar(self, id: int,request: AuxProdutoEstoqueUpdateRequest):
        estoque = self.est_service.buscar_por_id(request.id_estoque)

        if estoque is None:
            raise ValueError("Valor de Estoque não encontrado!")

        produto = self.prod_service.buscar_por_id(request.id_produto)

        if produto is None:
            raise ValueError("Valor do Produto não encontrado!")

        aux = self.aux_repository.find_by_id(id)

        if aux is None:
            raise ValueError("Vínculo estoque+produto não encontrado")

        aux.id_estoque = estoque.id
        aux.id_produto = produto.id
        aux.quantidade = request.quantidade

        auxProdutoEstoqueAtualizado = self.aux_repository.update(aux)

        auditoria = Auditoria(
            tabela = "aux_produto_estoque",
            registro_id = auxProdutoEstoqueAtualizado.id,
            operacao = "UPDATE",
            data_operacao = datetime.now()
        )

        self.auditoria_repository.save(auditoria)

        return auxProdutoEstoqueAtualizado

    def deletar(self, aux_id:int):
        aux = self.aux_repository.find_by_id(aux_id)

        if aux is None:
            raise ValueError("Vínculo estoque+produto não encontrado")

        auxProdDeletado = self.aux_repository.delete(aux)

        auditoria = Auditoria(
            tabela = "aux_produto_estoque",
            registro_id = auxProdDeletado.id,
            operacao = "DELETE",
            data_operacao = datetime.now()
        )

        self.auditoria_repository.save(auditoria)

        return auxProdDeletado


        