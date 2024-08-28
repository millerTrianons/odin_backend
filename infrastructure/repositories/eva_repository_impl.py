from typing import AsyncIterator
from fastapi.responses import FileResponse
from core.failures import ParametersNotFound
from domain.repositories.eva_repository import EvaRepository
from infrastructure.data_sources.eva_data_source import EvaDataSource
from infrastructure.dtos.eva_dto import EvaDto
from presentation.eva_data import EvaDataAskIn, EvaDataAskOut, EvaDataSpeakIn


class EvaRepositoryImpl(EvaRepository):
    def __init__(
            self,
            data_source: EvaDataSource   
        ) -> None:

        self.data_source: EvaDataSource = data_source

    async def ask(self, content: EvaDataAskIn) -> EvaDataAskOut:

        content = EvaDto.from_eva_data_ask_in(content)

        if not content.question:
            raise ParametersNotFound()
        
        result = await self.data_source.ask(content)

        return result.to_eva_data_ask_out()
    
    def speak(self, content: EvaDataSpeakIn) -> AsyncIterator[bytes]:
        content = EvaDto.from_eva_speak_in(content)

        if not content.response:
            raise ParametersNotFound()

        return self.data_source.speak(content)
    
    async def add_prompt(self, prompt: str) -> None:
        return await self.data_source.add_prompt(prompt)
    
    async def reset_prompt_and_messages(self) -> None:
        return await self.data_source.reset_prompt_and_messages()