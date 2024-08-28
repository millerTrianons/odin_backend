from abc import ABC, abstractmethod
from typing import AsyncIterator

from fastapi.responses import FileResponse

from presentation.eva_data import EvaDataAskIn, EvaDataAskOut, EvaDataSpeakIn

class EvaRepository(ABC):
    @abstractmethod
    async def ask(self, content: EvaDataAskIn) -> EvaDataAskOut:
        raise NotImplementedError()
    
    @abstractmethod
    def speak(self, content: EvaDataSpeakIn) -> AsyncIterator[bytes]:
        raise NotImplementedError()
    
    @abstractmethod
    async def reset_prompt_and_messages(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def add_prompt(self, prompt: str) -> None:
        raise NotImplementedError()
    