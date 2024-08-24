from presentation.user_site_scrap_data import UserSiteScrapData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class UserSiteRouteScrap(SQLModel, table=True):
    __tablename__ = "user_site_route_scrap"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    scrap_description: str
    tag: str
    item_id: Optional[str]
    css_class: Optional[str]
    function_on_the_page: Optional[str]
    parent_uuid: Optional[str]
    title: Optional[str]
    content: Optional[str]
    user_site_route_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))
    
    def __init__(
        self,
        uuid: str,
        scrap_description: str,
        tag: str,
        item_id: Optional[str],
        css_class: Optional[str],
        function_on_the_page: Optional[str],
        parent_uuid: Optional[str],
        title: Optional[str],
        content: Optional[str],
        user_site_route_uuid: str,
    ):
        self.uuid = uuid
        self.item_id = item_id
        self.tag = tag
        self.css_class = css_class
        self.function_on_the_page = function_on_the_page
        self.parent_uuid = parent_uuid
        self.title = title
        self.content = content
        self.user_site_route_uuid = user_site_route_uuid
        self.scrap_description = scrap_description

    @staticmethod
    def from_entity(
            user_site_scrap_data: UserSiteScrapData,
            uuid_data: Optional[str]   
        ):
        return UserSiteRouteScrap(
            uuid=uuid_data if uuid_data else uuid.uuid4(),
            item_id=user_site_scrap_data.item_id,
            tag=user_site_scrap_data.tag,
            css_class=user_site_scrap_data.css_class,
            function_on_the_page=user_site_scrap_data.function_on_the_page,
            parent_uuid=user_site_scrap_data.parent_uuid,
            title=user_site_scrap_data.title,
            content=user_site_scrap_data.content,
            user_site_route_uuid=user_site_scrap_data.user_site_route_uuid,
            scrap_description=user_site_scrap_data.scrap_description,
        )
