
from pydantic import BaseModel

class EvaData(BaseModel):
    pass

class EvaDataAskIn(EvaData):
    question: str

class EvaDataAskOut(EvaData):
    response: str

class EvaDataSpeakIn(EvaData):
    response: str



