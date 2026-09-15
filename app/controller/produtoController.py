from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.model.dto.produtoCreateRequest import ProdutoCreateRequest
from app.model.dto.produtoResponse import ProdutoResponse
from app.model.dto.produtoUpdateRequest import ProdutoUpdateRequest
from app.repository.produtoRepository import ProdutoRepository
from app.service.produtoService import ProdutoService


router_produto = APIRouter(
    prefix="/produto",
    tags=["Produto"]
)


def get_service(
    db: Session = Depends(get_db)
):

    repository = ProdutoRepository(db)

    return ProdutoService(repository)


@router_produto.get(
    "/",
    response_model=list[ProdutoResponse]
)
def listar_produtos(
    service: ProdutoService = Depends(get_service)
):

    return service.listar()


@router_produto.get(
    "/{produto_id}",
    response_model=ProdutoResponse
)
def buscar_produto(
    produto_id: int,
    service: ProdutoService = Depends(get_service)
):

    try:

        return service.buscar_por_id(produto_id)

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router_produto.post(
    "/",
    response_model=ProdutoResponse,
    status_code=201
)
def criar_produto(
    produto: ProdutoCreateRequest,
    service: ProdutoService = Depends(get_service)
):

    return service.criar(produto)

@router_produto.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(
    produto_id: int,
    produto: ProdutoUpdateRequest,
    service: ProdutoService = Depends(get_service)
):
    try:
        return service.atualizar(produto_id, produto)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router_produto.delete("/{produto_id}", response_model=ProdutoResponse)
def deletar_produto(
    produto_id: int,
    service: ProdutoService = Depends(get_service)
):
    try:
        return service.deletar(produto_id)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )    