from typing import Optional

class UserSiteScrapEntity:
    css_class: Optional[str]
    item_id: Optional[str]
    scrap_description: str
    function_on_the_page: str
    parent_uuid: Optional[str]
    title: Optional[str]
    content: Optional[str]
    user_site_route_uuid: str

    def __init__(
        self,
        css_class: Optional[str],
        item_id: Optional[str],
        scrap_description: str,
        function_on_the_page: str,
        parent_uuid: Optional[str],
        title: Optional[str],
        content: Optional[str],
        user_site_route_uuid: str
    ):
        css_class: Optional[str] = css_class
        item_id: Optional[str] = item_id
        scrap_description: str = scrap_description
        function_on_the_page: str = function_on_the_page
        parent_uuid: Optional[str] = parent_uuid
        title: Optional[str] = title
        content: Optional[str] = content
        user_site_route_uuid: str = user_site_route_uuid

    def __eq__(self, o: object) -> bool:
        if isinstance(o, UserSiteScrapEntity):
            return True
        return False