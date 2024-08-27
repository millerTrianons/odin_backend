from abc import ABC, abstractmethod

from fastapi.responses import FileResponse

from infrastructure.dtos.eva_dto import EvaDto

class EvaDataSource(ABC):
    @abstractmethod
    async def ask(self, content: EvaDto) -> EvaDto:
        raise NotImplementedError()

    @abstractmethod
    async def speak(self, content: EvaDto) -> FileResponse:
        raise NotImplementedError()
    
    @abstractmethod
    async def add_prompt(self, prompt: str) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def reset_prompt_and_messages(self) -> None:
        raise NotImplementedError()