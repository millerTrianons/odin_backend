from typing import Optional, Union

from pydantic import BaseModel


class ParamsData(BaseModel):
    a: float
    b: float
    c: float

    def __str__(self):
        return f'{{"a": {self.a}, "b": {self.b}, "c": {self.c}}}'
