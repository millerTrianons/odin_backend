from abc import ABC, abstractmethod
from typing import Optional

from infrastructure.dtos.chat_message import ChatMessage

class ChatDataSource(ABC):
    @abstractmethod
    async def add_chat_message(self, api_key: str, chat_message: ChatMessage) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def start_run(self, api_key: str, chat_uuid: str, current_route_uuid: Optional[str]) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_status(self, run_id: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_response(self, run_id: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def cancel_run(self, run_id: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def create_chat(self, user_site_uuid: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_messages(self, chat_uuid: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_last_messages(self, chat_uuid: str, message_uuid: str) -> object:
        raise NotImplementedError()