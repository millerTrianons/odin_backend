from typing import Optional

class ChatMessageData:
    message: str
    device_origin: Optional[str]
    api_key: str
    chat_uuid: str

    def __init__(
        self,
        message: str,
        api_key: str,
        device_origin: Optional[str],
        chat_uuid: str
    ):
        self.message: str = message
        self.api_key: str = api_key
        self.device_origin: str = device_origin
        self.chat_uuid: str = chat_uuid


    def __eq__(self, o: object) -> bool:
        if isinstance(o, ChatMessageData):
            return True
        return False

