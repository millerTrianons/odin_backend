from typing import AsyncIterator
from fastapi.responses import FileResponse
from domain.repositories.eva_repository import EvaRepository
from presentation.eva_data import  EvaDataAskIn, EvaDataAskOut, EvaDataSpeakIn


class EvaUseCase:
    def __init__(self, evaRepository: EvaRepository) -> None:
        self.evaRepository: EvaRepository = evaRepository

    async def ask(self, content: EvaDataAskIn) -> EvaDataAskOut:
        return await self.evaRepository.ask(content)

    def speak(self, content: EvaDataSpeakIn)  -> AsyncIterator[bytes]:
        return self.evaRepository.speak(content)
    
    async def reset_prompt_and_messages(self) -> None:
        return await self.evaRepository.reset_prompt_and_messages()

    async def add_prompt(self, prompt: str) -> None:
        return await self.evaRepository.add_prompt(prompt)