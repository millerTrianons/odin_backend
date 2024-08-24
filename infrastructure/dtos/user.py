from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt

class User(SQLModel, table=True):
    __tablename__ = "user_"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    user_email: str
    created_at: Optional[datetime] = Field(default=datetime.now())

    def __init__(self, uuid: str, user_email: str) -> None:
        self.uuid=uuid
        self.user_email=user_email