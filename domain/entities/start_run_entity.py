from typing import Optional

class StartRunEntity:
    api_key: str 
    chat_uuid: str
    current_route_uuid: str

    def __init__(
        self,
        api_key: str,
        chat_uuid: str,
        current_route_uuid: str,
    ):
        self.api_key: str = api_key
        self.chat_uuid: str = chat_uuid
        self.type: str = current_route_uuid

    def __eq__(self, o: object) -> bool:
        if isinstance(o, StartRunEntity):
            return True
        return False