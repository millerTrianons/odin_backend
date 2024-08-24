from presentation.api_access_data import ApiAccessData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class ApiAccess(SQLModel, table=True):
    __tablename__ = "api_access"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    api_access_description: str
    api_access_method: str
    api_access_path: str
    user_site_route_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))

    def __init__(
            self,
            uuid: str,
            api_access_description: str,
            api_access_method: str,
            api_access_path: str,
            user_site_route_uuid: str,
                 ) -> None:
        self.uuid = uuid
        self.api_access_description = api_access_description
        self.api_access_method = api_access_method
        self.api_access_path = api_access_path
        self.user_site_route_uuid = user_site_route_uuid
    
    @staticmethod
    def from_entity(
            api_access_data: ApiAccessData,
            uuid_data: str | None
        ):
        return ApiAccess(
            uuid=uuid_data if uuid_data else uuid.uuid4(),
            api_access_description=api_access_data.description,
            api_access_method=api_access_data.method,
            api_access_path=api_access_data.path,
            user_site_route_uuid=api_access_data.user_site_route_uuid,
        )
