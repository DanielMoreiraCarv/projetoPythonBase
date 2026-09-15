from fastapi import FastAPI

from app.controller.produtoController import router

app = FastAPI(title = "Gestão de Patrimônio", description = "API para gestão de patrimônio e Almoxarifado", version = "1.0.0")

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Gestão de Patrimônio!"}

app.include_router(router, prefix="/produto", tags=["Produto"])