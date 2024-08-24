from pydantic import BaseModel

class ApiAccessParameterData(BaseModel):
    api_access_uuid: str
    name: str
    type: str

class ApiAccessData(BaseModel):
    method: str
    path: str
    description: str
    user_site_route_uuid: str

class ApiAccessHeaderData(BaseModel):
    header: str
    content: str
    api_access_uuid: str
