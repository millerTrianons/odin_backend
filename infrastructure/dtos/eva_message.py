from datetime import datetime
from typing import Any, Dict, Optional, Tuple
from sqlmodel import Field, SQLModel


class EvaMessage(SQLModel, table=True):
    __tablename__ = "eva_message"

    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    role: int
    created_at: Optional[datetime] = Field(default=datetime.now())

    def __init__(
            self, 
            content: str,
            role: int
        ) -> None:
        self.content = content
        self.role = role