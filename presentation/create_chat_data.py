from pydantic import BaseModel

class CreateChatData(BaseModel):
    user_site_uuid: str