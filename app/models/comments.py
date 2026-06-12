from sqlalchemy import String, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db_async import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.teachers import Teacher
    from app.models.assignments import Assignment

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    teacher_name: Mapped[String] = mapped_column(String(255), nullable=False)
    assignment_id: Mapped[int] = mapped_column(ForeignKey("assignments.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Relationships
    assignment: Mapped["Assignment"] = relationship("Assignment", back_populates="comments", lazy="joined")