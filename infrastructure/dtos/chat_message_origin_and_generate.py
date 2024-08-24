from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt

class ChatMessageOriginAndGenerate(SQLModel, table=True):
    __tablename__ = 'chat_message_origin_and_generate'

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    origin_uuid: str
    generate_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))

    def __init__(
        self,
        uuid: str,
        origin_uuid: str,
        generate_uuid: str
    ):
        self.uuid = uuid
        self.origin_uuid = origin_uuid
        self.generate_uuid = generate_uuid