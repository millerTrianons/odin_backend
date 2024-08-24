from pydantic import BaseModel

class CreateSiteRouteData(BaseModel):
    route_url: str
    route_description: str
    user_site_uuid: str