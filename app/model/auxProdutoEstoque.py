from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, func, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class AuxProdutoEstoque(Base):
    __tablename__ = "py_aux_produto_estoque"

    id = Column(BigInteger, primary_key=True, index=False)

    id_estoque = Column(
        BigInteger,
        ForeignKey("py_estoque.id")
    )

    estoque = relationship("Estoque")

    id_produto = Column(
        BigInteger,
        ForeignKey("py_produto.id")
    )

    produto = relationship("Produto")

    quantidade = Column(Integer, nullable=False)