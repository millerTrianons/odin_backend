from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

from presentation.chat_message_data import ChatMessageData

class ChatMessage(SQLModel, table=True):
    __tablename__ = "chat_message"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    chat_uuid: str
    device_origin: Optional[str]
    tool_call: Optional[str]
    content: Optional[str]
    chat_role: str
    created_at: Optional[datetime] = Field(default=datetime.now())

    def __init__(
            self, 
            uuid: str, 
            chat_uuid: str, 
            device_origin: Optional[str],
            tool_call: Optional[str], 
            content: Optional[str],
            chat_role: str
        ) -> None:
        self.uuid= uuid 
        self.chat_uuid= chat_uuid
        self.content=content
        self.tool_call = tool_call
        self.device_origin = device_origin
        self.chat_role=chat_role

    @staticmethod
    def from_domain(message: ChatMessageData):
    
        return ChatMessage(
            uuid=uuid.uuid4(),
            device_origin=message.device_origin,
            content=message.message,
            chat_role='user',
            chat_uuid=message.chat_uuid,
            tool_call=None
        )



