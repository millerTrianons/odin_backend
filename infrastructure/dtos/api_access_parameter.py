from presentation.api_access_data import ApiAccessParameterData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class ApiAccessParameter(SQLModel, table=True):
    __tablename__ = 'api_access_parameter'

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    parameter_type: str
    parameter_name: str
    external_api_access_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))

    def __init__(
        self,
        uuid: str,
        parameter_type: str,
        parameter_name: str,
        external_api_access_uuid: str,
    ) -> None:
        self.uuid = uuid
        self.parameter_type = parameter_type
        self.parameter_name = parameter_name
        self.external_api_access_uuid = external_api_access_uuid

    @staticmethod
    def fromEntity(
            api_access_parameter_data: ApiAccessParameterData,
            uuid_data: str | None
        ):
        return ApiAccessParameter(
            uuid=uuid_data if uuid_data else uuid.uuid4(),
            parameter_type=api_access_parameter_data.type,
            parameter_name=api_access_parameter_data.name,
            external_api_access_uuid=api_access_parameter_data.api_access_uuid
        )
    