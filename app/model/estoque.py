from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, func, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Estoque(Base):
    __tablename__ = "py_estoque"

    id = Column(BigInteger, primary_key=True, index=True)
    
    cep = Column(String(8),nullable=True )

    numero_local = Column(Integer, nullable=True)

    telefone = Column(String(20), nullable=True)

    data_criacao: Mapped[datetime | None] = mapped_column(
        "dt_criacao",
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    data_atualizacao: Mapped[datetime | None] = mapped_column(
        "dt_alteracao",
        DateTime
    )

    data_delecao: Mapped[datetime | None] = mapped_column(
        "dt_delecao",
        DateTime
    )