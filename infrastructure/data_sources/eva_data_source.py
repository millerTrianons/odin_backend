from abc import ABC, abstractmethod
from typing import AsyncIterator

from fastapi.responses import FileResponse

from infrastructure.dtos.eva_dto import EvaDto

class EvaDataSource(ABC):
    @abstractmethod
    async def ask(self, content: EvaDto) -> EvaDto:
        raise NotImplementedError()

    @abstractmethod
    def speak(self, content: EvaDto)  -> AsyncIterator[bytes]:
        raise NotImplementedError()
    
    @abstractmethod
    async def add_prompt(self, prompt: str) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def reset_prompt_and_messages(self) -> None:
        raise NotImplementedError()