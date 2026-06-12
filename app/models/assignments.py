from sqlalchemy import String, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db_async import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.comments import Comment

class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    subject: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    student_name: Mapped[String] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Relationships
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="assignment", lazy="selectin")