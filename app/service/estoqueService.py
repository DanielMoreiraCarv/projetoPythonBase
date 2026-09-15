import datetime
from app.model.dto.estoqueCreateRequest import EstoqueCreateRequest
from app.model.estoque import Estoque
from app.model.dto.estoqueUpdateRequest import EstoqueUpdateRequest
from app.repository.estoqueRepository import EstoqueRepository

class EstoqueService:
    def __init__(self, estoque_repository: EstoqueRepository):
        self.estoque_repository = estoque_repository

    def listar(self):
        return self.estoque_repository.find_all()

    def criar(self, request: EstoqueCreateRequest):
        estoque = Estoque(
            cep = request.cep,
            numero_local = request.numero_local,
            telefone = request.telefone
        )

        return self.estoque_repository.save(estoque)

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
        estoque.cep = refresh.cep
        estoque.numero_local = request.numero_local
        estoque.data_atualizacao = datetime.now()

        return self.estoque_repository.update(estoque)

    def deletar(self, estoque_id: int):
        estoque = self.estoque_repository.find_by_id(estoque_id)

        if estoque is None:
            raise ValueError("Estoque não encontrado")

        if estoque.data_delecao is not None:
            raise ValueError("Estoque já foi deletado")

        return self.estoque_repository.delete(estoque)