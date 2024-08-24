from typing import Optional
from pydantic import BaseModel

class UserSiteScrapData(BaseModel):
    css_class: Optional[str]
    item_id: Optional[str]
    tag: str
    scrap_description: str
    function_on_the_page: str
    parent_uuid: Optional[str]
    title: Optional[str]
    content: Optional[str]
    user_site_route_uuid: str

class UserSiteScrapDataBody(BaseModel):
    user_site_route_uuid: str
    content: list[UserSiteScrapData]
