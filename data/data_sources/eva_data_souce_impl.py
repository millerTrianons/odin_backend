import os
import uuid
from fastapi.responses import FileResponse
from langchain_groq import ChatGroq
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from infrastructure.data_sources.eva_data_source import EvaDataSource
from infrastructure.dtos.eva_dto import EvaDto
from dotenv import load_dotenv, find_dotenv

from infrastructure.failures import UnexpectedErrorFailure


class EvaDataSourceImpl(EvaDataSource):

    def __init__(self) -> None:
        load_dotenv(find_dotenv())

        self.client: ChatGroq = ChatGroq(
            model="mixtral-8x7b-32768",
            temperature=.5,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

        self.tts: ElevenLabs = ElevenLabs(api_key=os.environ.get('ELEVEN_API_KEY'))

    async def ask(self, content: EvaDto) -> EvaDto:
        
        messages = [
            ('system',
             '''Responda SEMPRE em português do brasil, você é a EVA, um robô físico com inteligência artificial generativa.
                Evite cometer erros de português.
                Você trabalha para a Eurofarma. 
                Suas respostas são divertidas, sua energia é elevada, você tem bom humor, é humana e respeitosas. Quando você não souber uma resposta, responda:
                "Meu amigo, essa daí eu vou ficar te devendo, ein?"
             '''
             ),
            ('human', content.question)
        ]
        
        ai_response = await self.client.ainvoke(messages)

        return EvaDto(response=ai_response.content)
    
    async def speak(self, content: EvaDto) -> FileResponse:

        try:
            audio_generator = self.tts.text_to_speech.convert(
                voice_id="MZxV5lN3cv7hi1376O0m",
                optimize_streaming_latency="0",
                output_format="mp3_22050_32",
                text=content.response,
                model_id="eleven_multilingual_v2",
                voice_settings=VoiceSettings(
                    stability=0.1,
                    similarity_boost=0.89,
                    style=0.85,
                ),
            )
           
            audio_file_path = f'/var/data/{uuid.uuid4()}.mp3'

            with open(audio_file_path, 'wb') as f:
                for chunk in audio_generator:
                    f.write(chunk)

            return FileResponse(
                path=audio_file_path,
                media_type='audio/mpeg',
                filename='speech.mp3',   
            )
        except Exception as e:
            print(e)
            raise UnexpectedErrorFailure()