from sqlalchemy.orm import Session
from datetime import datetime
from app.model.auxProdutoEstoque import AuxProdutoEstoque

class AuxProdutoEstoqueRepository:
    def __init__(self,db:Session):
        self.db = db
    
    def find_all(self):
        return self.db.query(AuxProdutoEstoque).all()

    def find_by_estoque_id(self,estoque_id: int):
        return (self.db.query(AuxProdutoEstoque).filter(AuxProdutoEstoque.id_estoque==estoque_id).all())

    def find_by_produto_and_estoque(self, estoque_id: int, produto_id: int):
        return (self.db.query(AuxProdutoEstoque).filter(AuxProdutoEstoque.id_produto == produto_id,AuxProdutoEstoque.id_estoque == estoque_id).all())

    def find_by_id(self, id: int):
        return(self.db.query(AuxProdutoEstoque).filter(AuxProdutoEstoque.id == id).first())

    def save(self, aux: AuxProdutoEstoque):
        self.db.add(aux)
        self.db.commit()
        self.db.refresh(aux)

        return aux

    def update(self, aux: AuxProdutoEstoque):
        self.db.commit()
        self.db.refresh(aux)
        return aux
    
    def delete(self,aux: AuxProdutoEstoque):
        self.db.delete(aux)
        self.db.commit()
        return aux