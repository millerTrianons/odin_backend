class ApiAccessParameterEntity:
    api_access_uuid: str
    name: str
    type: str

    def __init__(
        self,
        api_access_uuid: str,
        name: str,
        type: str
    ):
        self.api_access_uuid: str = api_access_uuid
        self.name: str = name
        self.type: str = type


    def __eq__(self, o: object) -> bool:
        if isinstance(o, ApiAccessParameterEntity):
            return True
        return False

class ApiAccessEntity:
    method: str
    path: str
    description: str
    user_site_route_uuid: str

    def __init__(
        self,
        method: str,
        path: str,
        description: str,
        user_site_route_uuid: str,
    ):
        self.method: str = method
        self.path: str = path
        self.description: str = description
        self.user_site_route_uuid: str = user_site_route_uuid


    def __eq__(self, o: object) -> bool:
        if isinstance(o, ApiAccessEntity):
            return True
        return False

class ApiAccessHeaderEntity:
    header: str
    content: str
    api_access_uuid: str

    def __init__(
        self,
        header: str,
        content: str,
        api_access_uuid: str,
    ):
        self.header: str = header
        self.content: str = content
        self.api_access_uuid: str = api_access_uuid


    def __eq__(self, o: object) -> bool:
        if isinstance(o, ApiAccessParameterEntity):
            return True
        return False
