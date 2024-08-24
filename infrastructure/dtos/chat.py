from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt

class Chat(SQLModel, table=True):
    __tablename__ = "chat"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    user_site_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))

    def __init__(
            self, 
            uuid: str, 
            user_site_uuid: str
        ) -> None:
        self.uuid = uuid
        self.user_site_uuid = user_site_uuid

    