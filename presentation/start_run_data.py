from typing import Optional
from pydantic import BaseModel

class StartRunData(BaseModel):
    api_key: str 
    chat_uuid: str
    current_route_uuid: Optional[str]