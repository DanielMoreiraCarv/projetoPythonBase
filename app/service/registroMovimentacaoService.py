
from app.model.dto.registroMovimentacaoCreateRequest import RegistroMovimentacaoCreateRequest
from app.model.dto.registroMovimentacaoUpdateRequest import RegistroMovimentacaoUpdateRequest
from app.model.registroMovimentacao import RegistroMovimentacao
from app.repository.registroMovimentacaoRepository import RegistroMovimentacaoRepository
from app.service.estoqueService import EstoqueService
from app.service.produtoService import ProdutoService

class RegistroMovimentacaoService:
    def __init__(self, repository: RegistroMovimentacaoRepository, prod_service: ProdutoService, est_service: EstoqueService):
        self.repository = repository
        self.prod_service = prod_service
        self.est_service = est_service
    
    def listar(self):
        return self.repository.find_all()

    def buscar_por_id(self, id: int):
        registro = self.repository.find_by_id(id)

        if registro is None:
            raise ValueError("Registro de Movimentação não encontrado")

        return registro

    def buscar_por_produto(self, produto_id: int):
        registros = self.repository.find_by_id_produto(produto_id)

        if not registros:
            raise ValueError("Nenhum registro de movimentação encontrado para o produto informado")

        return registros

    def buscar_por_estoque(self, estoque_id: int):
        registros = self.repository.find_by_id_estoque(estoque_id)

        if not registros:
            raise ValueError("Nenhum registro de movimentação encontrado para o estoque informado")

        return registros

    def buscar_por_produto_e_estoque(self, produto_id: int, estoque_id: int):
        registros = self.repository.find_by_produto_and_estoque(produto_id, estoque_id)

        if not registros:
            raise ValueError("Nenhum registro de movimentação encontrado para o produto e estoque informados")

        return registros

    def criar(self, request: RegistroMovimentacaoCreateRequest):
        produto = self.prod_service.find_by_id(request.id_produto)

        if produto is None:
            raise ValueError("Produto não encontrado")

        estoque_chegada = self.est_service.find_by_id(request.id_estoque_chegada)

        estoque_saida = self.est_service.find_by_id(request.id_estoque_saida)

        if(request.tip_movimentacao == 0):
                            if estoque_chegada is None:
                                raise ValueError("Estoque de chegada não encontrado")
                            if estoque_saida is not None:
                                raise ValueError("Estoque de saída não deve ser informado para esse tipo de movimentação")
        elif(request.tip_movimentacao == 1):
                            if estoque_chegada is None:
                                raise ValueError("Estoque de chegada não encontrado")
                            if estoque_saida is None:
                                raise ValueError("Estoque de saída não encontrado")
        elif(request.tip_movimentacao == 2):
                            if estoque_saida is None:
                                raise ValueError("Estoque de saída não encontrado")
                            if estoque_chegada is not None:
                                raise ValueError("Estoque de chegada não deve ser informado para esse tipo de movimentação")

        registro = RegistroMovimentacao(
            id_produto=produto.id,
            id_estoque_chegada=estoque_chegada.id if request.tip_movimentacao == 0 or request.tip_movimentacao == 1 else None,
            id_estoque_saida=estoque_saida.id if request.tip_movimentacao == 1 or request.tip_movimentacao == 2 else None,
            quantidade=request.quantidade,
            dsc_responsavel=request.dsc_responsavel,
            tip_movimentacao=request.tip_movimentacao
        )

        return self.repository.save(registro)

    def atualizar(self, id: int, request: RegistroMovimentacaoUpdateRequest):
        registro = self.repository.find_by_id(id)

        if registro is None:
            raise ValueError("Registro de Movimentação não encontrado")

        produto = self.prod_service.find_by_id(request.id_produto)

        if produto is None:
            raise ValueError("Produto não encontrado")

        estoque_chegada = self.est_service.find_by_id(request.id_estoque_chegada)

        estoque_saida = self.est_service.find_by_id(request.id_estoque_saida)

        if(request.tip_movimentacao == 0):
                    if estoque_chegada is None:
                        raise ValueError("Estoque de chegada não encontrado")
                    if estoque_saida is not None:
                        raise ValueError("Estoque de saída não deve ser informado para esse tipo de movimentação")
        elif(request.tip_movimentacao == 1):
                    if estoque_chegada is None:
                        raise ValueError("Estoque de chegada não encontrado")
                    if estoque_saida is None:
                        raise ValueError("Estoque de saída não encontrado")
        elif(request.tip_movimentacao == 2):
                    if estoque_saida is None:
                        raise ValueError("Estoque de saída não encontrado")
                    if estoque_chegada is not None:
                        raise ValueError("Estoque de chegada não deve ser informado para esse tipo de movimentação")

        registro.id_produto = produto.id
        registro.id_estoque_chegada = estoque_chegada.id if request.tip_movimentacao == 0 or request.tip_movimentacao == 1 else None
        registro.id_estoque_saida = estoque_saida.id if request.tip_movimentacao == 1 or request.tip_movimentacao == 2 else None
        registro.quantidade = request.quantidade
        registro.dsc_responsavel = request.dsc_responsavel
        registro.tip_movimentacao = request.tip_movimentacao

        return self.repository.update(registro)

    def deletar(self, id: int):
        registro = self.repository.find_by_id(id)

        if registro is None:
            raise ValueError("Registro de Movimentação não encontrado")

        return self.repository.delete(registro)