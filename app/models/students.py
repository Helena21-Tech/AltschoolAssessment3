from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db_async import Base
from datetime import datetime

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

   