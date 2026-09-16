from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.model.dto.auxProdutoEstoqueCreateRequest import AuxProdutoEstoqueCreateRequest
from app.model.dto.auxProdutoEstoqueUpdateRequest import AuxProdutoEstoqueUpdateRequest
from app.model.dto.auxProdutoEstoqueResponse import AuxProdutoEstoqueResponse
from app.repository.auxProdutoEstoqueRepository import AuxProdutoEstoqueRepository
from app.service.auxProdutoEstoqueService import AuxProdutoEstoqueService
from app.repository.produtoRepository import ProdutoRepository
from app.service.produtoService import ProdutoService
from app.repository.estoqueRepository import EstoqueRepository
from app.service.estoqueService import EstoqueService
from app.repository.auditoriaRepository import AuditoriaRepository

router_aux = APIRouter(prefix="/aux",tags=["Aux"])

def get_service(db: Session = Depends(get_db)):
    auditoria_repository = AuditoriaRepository(db)
    repositoy_prod = ProdutoRepository(db)
    prod_service = ProdutoService(repositoy_prod,auditoria_repository)

    repository_est = EstoqueRepository(db)
    est_service = EstoqueService(repository_est,auditoria_repository)

    repository = AuxProdutoEstoqueRepository(db)

    return AuxProdutoEstoqueService(repository,prod_service,est_service,auditoria_repository)


@router_aux.get("/",response_model=list[AuxProdutoEstoqueResponse])
def listar_auxs(service: AuxProdutoEstoqueService = Depends(get_service)):
    return service.listar()

@router_aux.get("/estoque/{estoque_id}",response_model=list[AuxProdutoEstoqueResponse])
def listar_aux_por_estoque(estoque_id:int ,service: AuxProdutoEstoqueService = Depends(get_service)):
    try:
        return service.listar_por_estoque(estoque_id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_aux.get("/buscar/{id}",response_model=AuxProdutoEstoqueResponse)
def find_by_id(id: int, service: AuxProdutoEstoqueService = Depends(get_service)):
    try:
        return service.buscar_aux_por_id(id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_aux.get("/estoque/{estoque_id}/produto/{produto_id}",response_model=list[AuxProdutoEstoqueResponse])
def buscar_aux(estoque_id: int, produto_id: int, service: AuxProdutoEstoqueService = Depends(get_service)):
    try:
        return service.buscar_aux(estoque_id,produto_id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_aux.post("/",response_model=AuxProdutoEstoqueResponse)
def criar_aux(aux: AuxProdutoEstoqueCreateRequest, service: AuxProdutoEstoqueService = Depends(get_service)):
    return service.criar(aux)

@router_aux.put("/{id}",response_model=AuxProdutoEstoqueResponse)
def atualizar_aux(id: int, request:AuxProdutoEstoqueUpdateRequest,service: AuxProdutoEstoqueService = Depends(get_service)):
    try:
        return service.atualizar(id,request)
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_aux.delete("/{id}",response_model=AuxProdutoEstoqueResponse)
def delete_aux(id: int, service: AuxProdutoEstoqueService = Depends(get_service)):
    try:
        return service.deletar(id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))