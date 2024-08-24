from domain.repositories.chat_repository import ChatRepository
from presentation.start_run_data import StartRunData
from presentation.chat_message_data import ChatMessageData

class ChatUsecase:
    def __init__(self, chatRepository: ChatRepository) -> None:
        self.chatRepository = chatRepository

    async def add_message(self, content: ChatMessageData) -> object:
        return await self.chatRepository.add_chat_message(content)
    
    async def start_run(self, content: StartRunData) -> object:
        return await self.chatRepository.start_run(
            api_key = content.api_key, 
            chat_uuid = content.chat_uuid,
            current_route_uuid=content.current_route_uuid
        )
    
    async def get_status(self, run_id: str) -> object:
        return await self.chatRepository.get_status(run_id)
    
    async def get_response(self, run_id: str) -> object:
        return await self.chatRepository.get_response(run_id)
    
    async def cancel_run(self, run_id: str) -> object:
        return await self.chatRepository.cancel_run(run_id)
    
    async def create_chat(self, user_site_uuid: str) -> object:
        return await self.chatRepository.create_chat(user_site_uuid)
    
    async def get_messages(self, chat_uuid: str) -> object:
        return await self.chatRepository.get_messages(chat_uuid)
    
    async def get_last_messages(self, chat_uuid: str, message_uuid: str) -> object:
        return await self.chatRepository.get_last_messages(chat_uuid, message_uuid)