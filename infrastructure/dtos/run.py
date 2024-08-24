from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt

class Run(SQLModel, table=True):
    __tablename__ = "run"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    running_status: str
    chat_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now())

    def __init__(
            self, 
            uuid: str, 
            running_status: str, 
            chat_uuid: str
        ) -> None:
        self.uuid = uuid
        self.running_status = running_status
        self.chat_uuid = chat_uuid