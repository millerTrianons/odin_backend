from fastapi.responses import FileResponse
from domain.repositories.eva_repository import EvaRepository
from presentation.eva_data import  EvaDataAskIn, EvaDataAskOut, EvaDataSpeakIn


class EvaUseCase:
    def __init__(self, evaRepository: EvaRepository) -> None:
        self.evaRepository: EvaRepository = evaRepository

    async def ask(self, content: EvaDataAskIn) -> EvaDataAskOut:
        return await self.evaRepository.ask(content)

    async def response(self, content: EvaDataSpeakIn)-> FileResponse:
        return await self.evaRepository.speak(content)