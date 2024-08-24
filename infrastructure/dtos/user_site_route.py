from presentation.create_site_route_data import CreateSiteRouteData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class UserSiteRoute(SQLModel, table=True):
    __tablename__ = "user_site_route"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    route_url: str
    route_description: str
    user_site_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now())

    def __init__(
            self, 
            uuid: str, 
            route_url: str, 
            route_description: str, 
            user_site_uuid: str,   
        ) -> None:
        self.uuid = uuid
        self.route_url = route_url
        self.route_description = route_description
        self.user_site_uuid = user_site_uuid

    @staticmethod
    def from_entity(
            create_site_route_data: CreateSiteRouteData,
            uuid_data: Optional[str]
        ):
        return UserSiteRoute(
            uuid= uuid_data if uuid_data else uuid.uuid4(),
            route_url=create_site_route_data.route_url,
            route_description=create_site_route_data.route_description,
            user_site_uuid=create_site_route_data.user_site_uuid
        )