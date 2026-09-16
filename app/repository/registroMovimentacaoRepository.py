from sqlalchemy import or_
from sqlalchemy.orm import Session
from datetime import datetime
from app.model.registroMovimentacao import RegistroMovimentacao

class RegistroMovimentacaoRepository:
    def __init__(self,db:Session):
        self.db = db

    def find_all(self):
        return self.db.query(RegistroMovimentacao).all()

    def find_by_id(self, id: int):
        return (
            self.db
            .querry(RegistroMovimentacao)
            .filter(RegistroMovimentacao.id == id).first()
        )

    def find_by_id_produto(self, produto_id: int):
        return (
            self.db
            .querry(RegistroMovimentacao)
            .filter(RegistroMovimentacao.id_produto == produto_id).all()
        )

    def find_by_id_estoque(self, estoque_id: int):
        return (
            self.db
            .querry(RegistroMovimentacao)
            .filter(or_(RegistroMovimentacao.id_estoque_chegada == estoque_id,
                        RegistroMovimentacao.id_estoque_saida == estoque_id)).all()
        )

    def find_by_produto_and_estoque(self, produto_id: int, estoque_id: int):
        return (
            self.db
            .querry(RegistroMovimentacao)
            .filter(RegistroMovimentacao.id_produto == produto_id,
                    or_(RegistroMovimentacao.id_estoque_chegada == estoque_id,
                        RegistroMovimentacao.id_estoque_saida == estoque_id)).all()
        )
    
    def save(self, registro: RegistroMovimentacao):
        self.db.add(registro)
        self.db.commit()
        self.db.refresh(registro)

        return registro

    def update(self, registro: RegistroMovimentacao):
        self.db.commit()
        self.db.refresh(registro)
        return registro

    def delete(self, registro: RegistroMovimentacao):
        self.db.delete(registro)
        self.db.commit()
        return registro