from abc import ABC, abstractmethod

from fastapi.responses import FileResponse

from presentation.eva_data import EvaDataAskIn, EvaDataAskOut, EvaDataSpeakIn

class EvaRepository(ABC):
    @abstractmethod
    async def ask(self, content: EvaDataAskIn) -> EvaDataAskOut:
        raise NotImplementedError()
    
    @abstractmethod
    async def speak(self, content: EvaDataSpeakIn) -> FileResponse:
        raise NotImplementedError()
    