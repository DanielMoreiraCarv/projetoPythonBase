from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Auditoria(Base):
    __tablename__ = "py_auditoria"

    id = Column(BigInteger, primary_key=True, index=True)

    tabela = Column(String(100),nullable=False)

    registro_id = Column(BigInteger,nullable=False)

    operacao = Column(String,nullable=False)

    usuario = Column(String,nullable=False)

    descricao = Column(String(255))


    data_operacao: Mapped[datetime | None] = mapped_column(
        "dt_operacao",
        DateTime,
        server_default=func.now(),
        nullable=False
    )                     