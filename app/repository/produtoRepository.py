from sqlalchemy.orm import Session
from datetime import datetime

from app.model.produto import Produto


class ProdutoRepository:

    def __init__(self, db: Session):
        self.db = db

    def find_all(self):
        return self.db.query(Produto).filter(Produto.data_delecao.is_(None)).all()

    def find_by_id(self, produto_id: int):
        return (
            self.db
            .query(Produto)
            .filter(Produto.id == produto_id,
                    Produto.data_delecao.is_(None))
            .first()
        )

    def save(self, produto: Produto):
        self.db.add(produto)
        self.db.commit()
        self.db.refresh(produto)

        return produto

    def update(self, produto: Produto):
        self.db.commit()
        self.db.refresh(produto)
        return produto

    def delete(self, produto: Produto):
        produto.data_delecao = datetime.now()

        self.db.commit()
        self.db.refresh(produto)

        return produto