from presentation.create_site_data import CreateSiteData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class UserSite(SQLModel, table=True):
    __tablename__ = "user_site"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    site_url: str
    site_name: str
    site_description: str
    user_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now())

    def __init__(
            self, 
            uuid: str, 
            site_url: str, 
            site_name: str, 
            site_description: str, 
            user_uuid: str,
        ) -> None:
        self.uuid=uuid
        self.site_url = site_url
        self.site_name = site_name
        self.site_description = site_description
        self.user_uuid = user_uuid

    @staticmethod
    def from_entity(
            user_site_data: CreateSiteData,
            uuid_data: Optional[str]
        ):
        return UserSite(
            uuid= uuid_data if uuid_data else uuid.uuid4(), 
            site_url = user_site_data.site_url, 
            site_name = user_site_data.site_name, 
            site_description = user_site_data.site_description, 
            user_uuid = user_site_data.user_uuid,
        )