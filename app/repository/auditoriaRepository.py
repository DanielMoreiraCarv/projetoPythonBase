from sqlalchemy import or_
from sqlalchemy.orm import Session
from datetime import datetime
from app.model.auditoria import Auditoria

class AuditoriaRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self):
        return self.db.query(Auditoria).all()

    def find_by_id(self, id: int):
        return (
            self.db
            .query(Auditoria)
            .filter(Auditoria.id == id).first()
        )

    def find_by_tabela(self, tabela: str):
        return (
            self.db
            .query(Auditoria)
            .filter(Auditoria.tabela.like(f"%{tabela}%")).all()
        )

    def find_by_registro_id(self, registro_id: int):
        return (
            self.db
            .query(Auditoria)
            .filter(Auditoria.registro_id == registro_id).all()
        )

    def save(self, auditoria: Auditoria):
        self.db.add(auditoria)
        self.db.commit()
        self.db.refresh(auditoria)

        return auditoria

    def update(self, auditoria: Auditoria):
        self.db.commit()
        self.db.refresh(auditoria)
        return auditoria

    def delete(self, auditoria: Auditoria):
        self.db.delete(auditoria)
        self.db.commit()
        return auditoria