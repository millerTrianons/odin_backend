from datetime import datetime
from typing import Any, Dict, Optional, Tuple

from sqlmodel import Field, SQLModel


class EvaPrompt(SQLModel, table=True):
    __tablename__ = "eva_prompt"

    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    created_at: Optional[datetime] = Field(default=datetime.now())

    def __init__(self, content: str) -> None:
        self.content = content