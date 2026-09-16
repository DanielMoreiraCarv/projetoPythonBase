from datetime import datetime
from app.model.auditoria import Auditoria
from app.model.dto.estoqueCreateRequest import EstoqueCreateRequest
from app.model.estoque import Estoque
from app.model.dto.estoqueUpdateRequest import EstoqueUpdateRequest
from app.repository.estoqueRepository import EstoqueRepository
from app.repository.auditoriaRepository import AuditoriaRepository

class EstoqueService:
    def __init__(self, estoque_repository: EstoqueRepository, auditoria_repository: AuditoriaRepository):
        self.estoque_repository = estoque_repository
        self.auditoria_repository = auditoria_repository

    def listar(self):
        return self.estoque_repository.find_all()

    def criar(self, request: EstoqueCreateRequest):
        estoque = Estoque(
            cep = request.cep,
            numero_local = request.numero_local,
            telefone = request.telefone
        )

        estoque = self.estoque_repository.save(estoque)

        auditoria = Auditoria(
            tabela="estoque",
            registro_id=estoque.id,
            operacao="CREATE",
            data_operacao=datetime.now()
        )

        self.auditoria_repository.save(auditoria)

        return estoque

    def buscar_por_id(self, estoque_id: int):
        estoque = self.estoque_repository.find_by_id(estoque_id)

        if estoque is None:
            raise ValueError("Estoque não encontrado")

        return estoque

    def atualizar(self,estoque_id: int,request: EstoqueUpdateRequest):
        estoque = self.estoque_repository.find_by_id(estoque_id)

        if estoque is None:
            raise ValueError("Estoque não encontrado")

        if estoque.data_delecao is not None:
            raise ValueError("Estoque já foi deletado")

        estoque.telefone = request.telefone
        estoque.cep = request.cep
        estoque.numero_local = request.numero_local
        estoque.data_atualizacao = datetime.now()

        estoque_atualizado = self.estoque_repository.update(estoque)

        auditoria = Auditoria(
                tabela="estoque",
                registro_id=estoque.id,
                operacao="UPDATE",
                data_operacao=datetime.now()
        )
        
        self.auditoria_repository.save(auditoria)

        return estoque_atualizado

    def deletar(self, estoque_id: int):
        estoque = self.estoque_repository.find_by_id(estoque_id)

        if estoque is None:
            raise ValueError("Estoque não encontrado")

        if estoque.data_delecao is not None:
            raise ValueError("Estoque já foi deletado")

        estoque.data_delecao = datetime.now()

        estoque_deletado = self.estoque_repository.update(estoque)

        auditoria = Auditoria(
            tabela="estoque",
            registro_id=estoque.id,
            operacao="DELETE",
            data_operacao=datetime.now()
        )

        self.auditoria_repository.save(auditoria)

        return estoque_deletado