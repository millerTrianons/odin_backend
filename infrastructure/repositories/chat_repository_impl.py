from typing import Optional
from domain.repositories.chat_repository import ChatRepository
from infrastructure.data_sources.chat_data_source import ChatDataSource
from presentation.chat_message_data import ChatMessageData
from infrastructure.dtos.chat_message import ChatMessage

class ChatRepositoryImpl(ChatRepository):
    def __init__(self, chat_data_source=ChatDataSource):
        self.chat_data_source = chat_data_source

    async def add_chat_message(self, content: ChatMessageData) -> object:
        return await self.chat_data_source.add_chat_message(
            api_key=content.api_key,
            chat_message=ChatMessage.from_domain(content),
        )
    
    async def start_run(self, api_key: str, chat_uuid: str, current_route_uuid: Optional[str]) -> object:
        return await self.chat_data_source.start_run(api_key, chat_uuid, current_route_uuid)

    async def get_status(self, run_id: str) -> object:
        return await self.chat_data_source.get_status(run_id)

    async def get_response(self, run_id: str) -> object:
        return await self.chat_data_source.get_response(run_id)

    async def cancel_run(self, run_id: str) -> object:
        return await self.chat_data_source.cancel_run(run_id)
    
    async def create_chat(self, user_site_uuid: str) -> object:
        return await self.chat_data_source.create_chat(user_site_uuid)
    
    async def get_messages(self, chat_uuid: str) -> object:
        return await self.chat_data_source.get_messages(chat_uuid)
    
    async def get_last_messages(self, chat_uuid: str, message_uuid: str) -> object:
        return await self.chat_data_source.get_last_messages(chat_uuid, message_uuid)