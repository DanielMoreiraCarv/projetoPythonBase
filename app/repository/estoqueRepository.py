from sqlalchemy.orm import Session
from datetime import datetime
from app.model.estoque import Estoque

class EstoqueRepository:
    def __init__(self,db:Session):
        self.db = db

    def find_all(self):
        return self.db.query(Estoque).filter(Estoque.data_delecao.is_(None)).all()

    def find_by_id(self, estoque_id: int):
        return(
            self.db
            .query(Estoque)
            .filter(Estoque.id == estoque_id, Estoque.data_delecao.is_(None))
            .first()
        )      

    def save(self, estoque: Estoque):
        self.db.add(estoque)
        self.db.commit()
        self.db.refresh(estoque)

        return estoque

    def update(self,estoque: Estoque):
        self.db.commit()
        self.db.refresh(estoque)
        return estoque

    def delete(self,estoque: Estoque):
        estoque.data_delecao = datetime.now()

        self.db.commit()
        self.db.refresh(estoque)

        return estoque  