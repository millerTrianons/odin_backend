from typing import Optional

from presentation.eva_data import EvaDataAskIn, EvaDataAskOut, EvaDataSpeakIn

class EvaDto:
    question: Optional[str]
    response: Optional[str]

    def __init__(
            self, 
            question: Optional[str] = None,
            response: Optional[str] = None
        ) -> None:
        self.question = question
        self.response = response

    @staticmethod
    def from_eva_data_ask_in(content: EvaDataAskIn):
        return EvaDto(question=content.question)
    
    @staticmethod
    def from_eva_speak_in(content: EvaDataSpeakIn):
        return EvaDto(response=content.response)
    
    def to_eva_data_ask_out(self) -> EvaDataAskOut:
        return EvaDataAskOut(response=self.response)