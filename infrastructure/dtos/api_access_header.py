from presentation.api_access_data import ApiAccessHeaderData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class ApiAcessHeader(SQLModel, table=True):
    __tablename__ = 'api_access_header'

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    header: str
    content: str
    api_access_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))

    def __init__(
        self,
        id: Optional[int],
        uuid: str,
        header: str,
        content: str,
        api_access_uuid: str,
    ) -> None:
        self.id = id
        self.uuid = uuid
        self.header = header
        self.content = content
        self.api_access_uuid = api_access_uuid

    @staticmethod
    def fromEntity(
            api_access_header_data: ApiAccessHeaderData, 
            uuid_data: str | None
        ):
        return ApiAcessHeader(
            uuid=uuid_data if uuid_data else uuid.uuid4(),
            header=api_access_header_data.header,
            content=api_access_header_data.content,
            api_access_uuid=api_access_header_data.api_access_uuid
        )