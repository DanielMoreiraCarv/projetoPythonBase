from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.model.dto.registroMovimentacaoCreateRequest import RegistroMovimentacaoCreateRequest
from app.model.dto.registroMovimentacaoUpdateRequest import RegistroMovimentacaoUpdateRequest
from app.model.dto.registroMovimentacaoResponse import RegistroMovimentacaoResponse
from app.repository.registroMovimentacaoRepository import RegistroMovimentacaoRepository
from app.service.registroMovimentacaoService import RegistroMovimentacaoService
from app.repository.produtoRepository import ProdutoRepository
from app.service.produtoService import ProdutoService
from app.repository.estoqueRepository import EstoqueRepository
from app.service.estoqueService import EstoqueService

router_registro = APIRouter(prefix="/registro",tags=["Registro"])

def get_service(db: Session = Depends(get_db)):
    repositoy_prod = ProdutoRepository(db)
    prod_service = ProdutoService(repositoy_prod)

    repository_est = EstoqueRepository(db)
    est_service = EstoqueService(repository_est)

    repository = RegistroMovimentacaoRepository(db)

    return RegistroMovimentacaoService(repository,prod_service,est_service)

@router_registro.get("/",response_model=list[RegistroMovimentacaoResponse])
def listar_registros(service: RegistroMovimentacaoService = Depends(get_service)):
    return service.listar()

@router_registro.get("/buscar/{id}",response_model=RegistroMovimentacaoResponse)
def buscar_registro_por_id(id: int, service: RegistroMovimentacaoService = Depends(get_service)):
    try:
        return service.buscar_por_id(id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_registro.get("/produto/{produto_id}",response_model=list[RegistroMovimentacaoResponse])
def buscar_registro_por_produto(produto_id: int, service: RegistroMovimentacaoService = Depends(get_service)):
    try:
        return service.buscar_por_produto(produto_id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_registro.get("/estoque/{estoque_id}",response_model=list[RegistroMovimentacaoResponse])
def buscar_registro_por_estoque(estoque_id: int, service: RegistroMovimentacaoService = Depends(get_service)):
    try:
        return service.buscar_por_estoque(estoque_id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_registro.get("/produto/{produto_id}/estoque/{estoque_id}",response_model=list[RegistroMovimentacaoResponse])
def buscar_registro_por_produto_e_estoque(produto_id: int, estoque_id: int, service: RegistroMovimentacaoService = Depends(get_service)):
    try:
        return service.buscar_por_produto_e_estoque(produto_id, estoque_id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_registro.post("/",response_model=RegistroMovimentacaoResponse)
def criar_registro(request: RegistroMovimentacaoCreateRequest, service: RegistroMovimentacaoService = Depends(get_service)):
    try:
        return service.criar(request)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_registro.put("/{id}",response_model=RegistroMovimentacaoResponse)
def atualizar_registro(id: int, request: RegistroMovimentacaoUpdateRequest, service: RegistroMovimentacaoService = Depends(get_service)):
    try:
        return service.atualizar(id, request)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_registro.delete("/{id}",response_model=RegistroMovimentacaoResponse)
def deletar_registro(id: int, service: RegistroMovimentacaoService = Depends(get_service)):
    try:
        return service.deletar(id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))