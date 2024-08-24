from typing import Optional
from pydantic import BaseModel

class ChatMessageData(BaseModel):
    message: str
    api_key: str
    chat_uuid: str
    device_origin: Optional[str]