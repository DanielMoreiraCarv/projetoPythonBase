from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Produto(Base):
    __tablename__ = "py_produto"

    id = Column(BigInteger, primary_key=True, index=True)

    descricao = Column(String(255), nullable=True)

    marca = Column(String(255))

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