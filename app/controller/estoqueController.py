from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.model.dto.estoqueCreateRequest import EstoqueCreateRequest
from app.model.dto.estoqueUpdateRequest import EstoqueUpdateRequest
from app.model.dto.estoqueResponse import EstoqueResponse
from app.repository.estoqueRepository import EstoqueRepository
from app.service.estoqueService import EstoqueService
from app.repository.auditoriaRepository import AuditoriaRepository

router_estoque = APIRouter(prefix="/estoque",tags=["Estoque"])

def get_service(
    db:Session = Depends(get_db)
):
    auditoria_repository = AuditoriaRepository(db)
    repository = EstoqueRepository(db)

    return EstoqueService(repository, auditoria_repository)

@router_estoque.get("/",response_model=list[EstoqueResponse])
def listar_estoques(service: EstoqueService = Depends(get_service)):
    return service.listar()

@router_estoque.get("/{estoque_id}",response_model=EstoqueResponse)
def buscar_estoque(estoque_id: int,service: EstoqueService = Depends(get_service)):
    try:
        return service.buscar_por_id(estoque_id)

    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_estoque.post("/",response_model=EstoqueResponse,status_code=201)
def criar_estoque(estoque: EstoqueCreateRequest, service: EstoqueService = Depends(get_service)):
    return service.criar(estoque)

@router_estoque.put("/{estoque_id}",response_model=EstoqueResponse|None)
def atualizar_estoque(estoque_id: int, estoque: EstoqueUpdateRequest, service: EstoqueService = Depends(get_service)):
    try:
        return service.atualizar(estoque_id,estoque)
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@router_estoque.delete("/{estoque_id}",response_model=EstoqueResponse)
def deletar_estoque(estoque_id: int, service: EstoqueService = Depends(get_service)):
    try:
        return service.deletar(estoque_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))