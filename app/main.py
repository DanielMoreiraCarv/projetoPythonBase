from fastapi import FastAPI

from app.controller.produtoController import router_produto
from app.controller.estoqueController import router_estoque
from app.controller.auxProdutoEstoqueController import router_aux

app = FastAPI(title = "Gestão de Patrimônio", description = "API para gestão de patrimônio e Almoxarifado", version = "1.0.0")

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Gestão de Patrimônio!"}

app.include_router(router_produto, tags=["Produto"])
app.include_router(router_estoque,tags=["Estoque"])
app.include_router(router_aux,tags=["Aux"])