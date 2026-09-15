from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, func, int
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class RegistroMovimentacao(Base):
    __tablename__ = "py_registro_movimentacao"

    id = Column(BigInteger, primary_key=True, index=True)

    id_estoque_chegada = Column(
        BigInteger,
        ForeignKey("estoque.id")
    )

    estoque_chegada = relationship(
        "Estoque",
        foreign_keys=[id_estoque_chegada]
    )

    id_estoque_saida = Column(
        BigInteger,
        ForeignKey("estoque.id")
    )

    estoque_saida = relationship(
        "Estoque",
        foreign_keys=[id_estoque_saida]
    )
    

    id_produto = Column(
        BigInteger,
        ForeignKey("produto.id")
    )

    produto = relationship("Produto")

    quantidade = Column(int, nullable=True)

    data_movimentacao: Mapped[datetime | None] = mapped_column(
        "dt_movimentacao",
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    dsc_responsavel = Column(String(255),nullable=True)

    tip_movimentacao = Column(int,nullable=True)
