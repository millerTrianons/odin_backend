from infrastructure.data_sources.management_data_source import ManagementDataSource
from data.services.sql_connection_service import SqlConnectionService
from infrastructure.dtos.user_site import UserSite
from infrastructure.dtos.user_site_route import UserSiteRoute
from infrastructure.dtos.api_key import ApiKey
from data.services.user_site_route_scrap import UserSiteScrapService
import uuid
from infrastructure.dtos.user_site_route_scrap import UserSiteRouteScrap
from infrastructure.dtos.user_style_sheet import UserStyleSheet
from presentation.user_site_scrap_data import UserSiteScrapDataBody

class ManagementeDataSourceImpl(ManagementDataSource):
    def __init__(self) -> None:
        self.connection = SqlConnectionService()
        self.user_site_scrap_service = UserSiteScrapService()

    async def create_site_route(self, user_site_route: UserSiteRoute) -> object:
        await self.connection.insert([user_site_route])

        return { "uuid": user_site_route.uuid }
    
    async def create_user_site(self, content: UserSite) -> object:
        
        await self.connection.insert([content])

        return { "uuid": content.uuid }
    
    async def list_routes(self, user_site_uuid: str) -> object:
        statement = f"SELECT * FROM user_site_route WHERE user_site_uuid='{user_site_uuid}'"

        user_site_routes = await self.connection.get(statement)

        return {'data': [{
                'uuid': user_site_route[1], 
                'route': user_site_route[2], 
                'descritpion': user_site_route[3],
                'site_uuid': user_site_route[4],
                'created_at': user_site_route[5]
                } for user_site_route in user_site_routes]}
    
    async def list_sites(self, user_uuid: str) -> list[object]:
        statement = f"SELECT * FROM user_site WHERE user_uuid='{user_uuid}'"

        user_sites = await self.connection.get(statement)

        return {'data': [{
                'uuid': user_site[1], 
                'name': user_site[2], 
                'description': user_site[3], 
                'url': user_site[4],
                'created_at': user_site[6]
                } for user_site in user_sites]}
    
    async def list_chat_by_site(self, user_site_uuid: str) -> object:
        statement= f"""
            SELECT c.uuid, c.user_site_uuid
            FROM chat AS c
            JOIN user_site AS us ON c.user_site_uuid = us.uuid
            WHERE us.uuid = '{user_site_uuid}'
        """

        chats = await self.connection.get(statement)
        
        return {
            'quantity': len(chats),
            'data' : [
                {
                    'chat_uuid': chat[0],
                    'user_site_uuid': chat[1]
                } for chat in chats]
        }
    
    async def create_api_key(self, user_uuid: str) ->  object:
        api_key:  ApiKey = ApiKey(
            uuid=uuid.uuid4(),
            user_uuid=user_uuid
        )

        await self.connection.insert([api_key])

        return {'api_key': api_key.uuid}
    

    async def list_api_keys(self, user_uuid: str) -> object:
        statement = f"SELECT uuid, created_at FROM api_key WHERE user_uuid='{user_uuid}'"

        api_keys = await self.connection.get(statement)

        return {'data': [{
                'key': api_key[0], 
                'created_at': api_key[1]
                } for api_key in api_keys]}
    
    async def scrap_user_site_route(self, content: UserSiteScrapDataBody) -> object:
        statement = f"SELECT * FROM user_site_route WHERE uuid='{content.user_site_route_uuid}'"

        user_site_route_scrap_url = await self.connection.get_one(statement)


        if user_site_route_scrap_url :
            user_site_scraps: list[UserSiteRouteScrap] = []

            for user_site_scrap_data in content.content:
                user_site_scraps.append(UserSiteRouteScrap.from_entity(user_site_scrap_data, None))

            await self.connection.insert(user_site_scraps)
            
            return {'scraps': [item.uuid for item in user_site_scraps]}
        
        return {'failed': 'route not found'}
    
    async def list_scrap_by_user_site_route (self, user_site_route_uuid: str) -> object:
        statement = f"""
            SELECT uuid, tag, css_class, function_on_the_page, parent_uuid,
                title, content, scrap_description, user_site_route_uuid, created_at
            FROM user_site_route_scrap WHERE user_site_route_uuid='{user_site_route_uuid}'"""
        
        user_site_route_scraps = await self.connection.get(str(statement))

        return  {'data': [{
                'uuid': item[0],
                'tag': item[1],
                'css_class': item[2],
                'function_on_the_page': item[3],
                'parent_uuid': item[4],
                'title': item[5],
                'content': item[6],
                'scrap_description': item[7],
                'user_site_route_uuid': item[8],
                'created_at': item[9]
            } 
            for item in user_site_route_scraps]}
    
    async def get_user_site_route_uuid_by_url(self, url: str) -> object:
        statement = f"SELECT uuid FROM user_site_route WHERE route_url ILIKE '{url}%'"

        site_route_uuid = await self.connection.get_one(statement)

        if site_route_uuid:

            return {'data': {
                        'uuid':  site_route_uuid[0],
                        'url': url
                    }
                }
        
        return {'failed': 'route not found'}
    
    async def delete_site_route(self, uuid: str) -> None:
        statement = f"DELETE FROM user_site_route WHERE uuid='{uuid}'"

        await self.connection.update(statement)

    async def delete_site_route_scrap(self, uuid: str) -> None:
        statement = f"DELETE FROM user_site_route_scrap WHERE uuid='{uuid}'"

        await self.connection.update(statement)

    async def create_user_style_sheet(self, user_style_sheet: UserStyleSheet) -> object:
        await self.connection.insert([user_style_sheet])

        return {'data': {
                "user_site_style_sheet_uuid": user_style_sheet.uuid,
            },
        }
    
    async def list_user_style_sheets(self, user_uuid: str) -> object:
        statement = f"SELECT * FROM user_site_style_sheet WHERE user_site_uuid='{user_uuid}'"

        user_syle_sheets = await self.connection.get(statement)

        return {'data': [{
            'style_sheet_uuid': item[1],
            'style_sheet_url': item[2],
            'style_sheet_name': item[3],
            'style_sheet_description': item[4],
            'style_sheet_content': item[5],
            'user_uuid': item[6],
            'created_at': item[7],
        } for item in user_syle_sheets]}
    
    async def delete_style_sheet(self, uuid: str) -> None:
        statement = f"DELETE FROM user_site_style_sheet WHERE uuid='{uuid}'"

        await self.connection.update(statement)

    async def update_site(self, user_site: UserSite) -> object:

        statement = f"""
            UPDATE user_site
            SET site_name = '{user_site.site_name}',
                site_description = '{user_site.site_description}',
                site_url = '{user_site.site_url}'
            WHERE uuid = '{user_site.uuid}' AND user_uuid = '{user_site.user_uuid}' 
        """

        await self.connection.update(statement)

        return {"data": user_site.uuid}
    
    async def update_site_route(self, user_site_route: UserSiteRoute) -> object:
        statement = f"""
            UPDATE user_site_route
            SET route_url = '{user_site_route.route_url}',
                route_description = '{user_site_route.route_description}'
            WHERE uuid = '{user_site_route.uuid}' AND user_site_uuid = '{user_site_route.user_site_uuid}' 
        """

        await self.connection.update(statement)

        return {"data": user_site_route.uuid}
    
    async def update_site_style_sheet(self, user_site_style_sheet: UserStyleSheet)-> object:
        statement = f"""
            UPDATE user_site_style_sheet
            SET style_sheet_url = '{user_site_style_sheet.style_sheet_url}',
                style_sheet_name = '{user_site_style_sheet.style_sheet_name}',
                style_sheet_description = '{user_site_style_sheet.style_sheet_description}',
                style_sheet_content = '{user_site_style_sheet.style_sheet_content}'
            WHERE uuid = '{user_site_style_sheet.uuid}' AND user_site_uuid = '{user_site_style_sheet.user_site_uuid}' 
        """

        await self.connection.update(statement)

        return {"data": user_site_style_sheet.uuid}
    
    async def update_site_route_scrap(self, user_site_route_scrap: UserSiteRouteScrap) -> object:
        statement = f"""
            UPDATE user_site_route_scrap
            SET item_id = '{user_site_route_scrap.item_id}',
                tag = '{user_site_route_scrap.tag}',
                css_class = '{user_site_route_scrap.css_class}',
                function_on_the_page = '{user_site_route_scrap.function_on_the_page}',
                parent_uuid = '{user_site_route_scrap.parent_uuid}',
                title = '{user_site_route_scrap.title}',
                content = '{user_site_route_scrap.content}',
                scrap_description = '{user_site_route_scrap.scrap_description}'
            WHERE uuid = '{user_site_route_scrap.uuid}' AND user_site_route_uuid = '{user_site_route_scrap.user_site_route_uuid}' 
        """
        
        await self.connection.update(statement)

        return {"data": user_site_route_scrap.uuid}

