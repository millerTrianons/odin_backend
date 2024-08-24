from pydantic import BaseModel

class CreateSiteData(BaseModel):
    site_url: str
    site_name: str
    site_description: str
    user_uuid: str