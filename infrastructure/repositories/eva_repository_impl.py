from fastapi.responses import FileResponse
from domain.core.failures import ParametersNotFound
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
    
    async def speak(self, content: EvaDataSpeakIn) -> FileResponse:
        content = EvaDto.from_eva_speak_in(content)

        if not content.response:
            raise ParametersNotFound()

        return await self.data_source.speak(content)