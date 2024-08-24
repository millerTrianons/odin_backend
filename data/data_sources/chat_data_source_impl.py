from http.client import HTTPException
from typing import Optional
from infrastructure.data_sources.chat_data_source import ChatDataSource
from datetime import datetime
import asyncio
import uuid
import ast
import datetime as dt
from data.services.run_service import RunService
from data.services.sql_connection_service import SqlConnectionService
from infrastructure.dtos.chat_message import ChatMessage
from infrastructure.dtos.chat import Chat

class ChatDataSourceImpl(ChatDataSource):
    connection: SqlConnectionService
    run_service: RunService

    def __init__(self) -> None:
        self.connection = SqlConnectionService()
        self.run_service = RunService()

    async def add_chat_message(self, api_key: str, chat_message: ChatMessage) -> object:
        statement = f"SELECT uuid from api_key where uuid='{api_key}'"

        if(await self.connection.get_one(statement) is None):
            return { 'error': 'invalid api key'}

        await self.connection.insert([chat_message])

        return  {
            'chat_id': chat_message.chat_uuid,
            'data': {
                'id': chat_message.uuid, 
                'chat_uuid': chat_message.chat_uuid, 
                'toll_call': chat_message.tool_call, 
                'message': chat_message.content, 
                'role': chat_message.chat_role,
                'device_origin': chat_message.device_origin,
                'created_at': datetime.now(dt.UTC),
            }
        }
    
    async def start_run(self, api_key: str, chat_uuid: str, current_route_uuid: Optional[str]) -> object:
        statement = f"SELECT uuid from api_key where uuid='{api_key}'"

        if await self.connection.get_one(statement) is None:
            return { 'error': 'invalid api key'}
        
        run_uuid = uuid.uuid4()
        
        statement = f"""
            SELECT usr.route_url, usr.route_description, usr.created_at
            FROM user_site_route usr 
            JOIN chat c ON usr.user_site_uuid = c.user_site_uuid
            WHERE c.uuid = '{chat_uuid}'"""

        routes = await self.connection.get(statement)

        site_data = [{
            'route_url': route[0],
            'route_description': route[1],
            'created_at': route[2],
        } for route in routes]

        statement = f"""
            SELECT usss.style_sheet_url, usss.style_sheet_name, 
                usss.style_sheet_description, usss.style_sheet_content
            FROM user_site_style_sheet usss
            JOIN chat c ON usss.user_site_uuid = c.user_site_uuid
            WHERE c.uuid = '{chat_uuid}'"""

        user_style_sheets = await self.connection.get(statement)

        css_style_sheets = [{
            'style_sheet_url': user_style_sheet[0],
            'style_sheet_name': user_style_sheet[1],
            'style_sheet_description': user_style_sheet[2]
        } for user_style_sheet in user_style_sheets]
  
        route_scraps: list[object] = []

        current_route_url: Optional[str] = None

        if current_route_uuid:
            statement = f"""
                SELECT usrs.uuid, usrs.item_id, usrs.tag, usrs.css_class, usrs.function_on_the_page,
                    usrs.parent_uuid, usrs.title, usrs.content, usrs.scrap_description, 
                    usr.route_url
                FROM user_site_route_scrap usrs
                JOIN  user_site_route usr ON usr.uuid = usrs.user_site_route_uuid
                WHERE user_site_route_uuid='{current_route_uuid}'"""

            res = await self.connection.get(statement)

            route_scraps = [{
                'item_uuid': item[0],
                'item_id': item[1],
                'tag': item[2],
                'css_class': item[3],
                'function_on_the_page': item[4],
                'parent_uuid': item[5],
                'title': item[6],
                'content': item[7],
                'scrap_description': item[8],
                'route_url': item[9]
            } for item in res]

            statement = f"""SELECT route_url from user_site_route WHERE uuid='{current_route_uuid}'"""

            res = await self.connection.get_one(statement)

            if res:
                current_route_url = res[0]
            
        asyncio.create_task(self.run_service.run(
            run_uuid,
            chat_uuid,
            route_scraps,
            site_data,
            current_route_url,
            css_style_sheets
        ))
 
        return {  
            'run_uuid': run_uuid,
            'status': 'queued'
        }
    
    async def get_status(self, run_id: str) -> object:
        statement = f"SELECT * FROM run WHERE uuid='{run_id}' LIMIT 1"

        status = await self.connection.get_one(statement)

        return {
            'id': run_id,
            'status': status[2],
            'date': datetime.now(dt.UTC)
        }
    
    async def get_response(self, run_id: str) -> object:
        return {}
    
    async def cancel_run(self, run_id: str) -> object:
        return {
            'run_id': run_id,
        }
    
    async def get_messages(self, chat_uuid: str) -> object:
        statement = f"""
            SELECT uuid, chat_uuid, tool_call, content, chat_role, device_origin, created_at
            FROM chat_message 
            WHERE chat_uuid='{chat_uuid}';"""

        messages = await self.connection.get(statement)

        messages = [{
            'uuid': message[0], 
            'chat_uuid': message[1], 
            'toll_call': ast.literal_eval(message[2]) if message[2] else None, 
            'message': message[3], 
            'role': message[4],
            'device_origin': message[5],
            'created_at': message[6]
            } for message in messages]

        return messages
    

    async def get_last_messages(self, chat_uuid: str, message_uuid: str) -> object:

        statement = f"SELECT id FROM chat_message WHERE uuid='{message_uuid}' AND chat_uuid='{chat_uuid}'"
        
        message = await self.connection.get_one(statement)

        if message:

            statement = f"""
                SELECT uuid, chat_uuid, tool_call, content, chat_role, device_origin, created_at 
                FROM chat_message 
                WHERE chat_uuid='{chat_uuid}' AND id > {message[0]};"""

            messages = await self.connection.get(statement)

            messages = [{
                'uuid': message[0], 
                'chat_uuid': message[1], 
                'toll_call': ast.literal_eval(message[2]) if message[2] else None, 
                'message': message[3], 
                'role': message[4],
                'device_origin': message[5],
                'created_at': message[6]
                } for message in messages]

            return messages
        
        raise HTTPException(status_code=404, detail="last message not found")
    
    async def create_chat(self, user_site_uuid: str) -> object:
        try:
            chat: Chat = Chat(
                uuid=uuid.uuid4(), 
                user_site_uuid=user_site_uuid,
            )

            await self.connection.insert([chat])

            return {
                'chat_id': chat.uuid
            }
        except:
            raise HTTPException(status_code=404, detail="site not found")
    
    async def get_style_sheet_by_uuid(self, style_sheet_uuid: str) -> object:
        statement = f"SELECT * FROM user_style_sheet WHERE uuid='{style_sheet_uuid}'"

        style_sheet = await self.connection.get_one(statement)
        
        print(style_sheet)

        return {}
    
        
        