from infrastructure.data_sources.ai_manager_data_source import AIManagerDatasource
from fastapi import UploadFile, File
import requests
import numpy as np
from bs4 import BeautifulSoup

from data.services.sql_connection_service import SqlConnectionService

class AIManagerDataSourceImpl(AIManagerDatasource):
    def __init__(self) -> None:
        self.connection = SqlConnectionService()

    async def list_ais(self, user_id: str, offset: int = 0, quantity: int = 10) -> list[object]:
        return {}
    
    async def train_ai(self, api_key: str, file: UploadFile = File(...)) -> object:
      
        return {}
    
    async def scrap_user_site_route(self, user_site_route_uuid: str) -> object:

        statement = f"""SELECT route_url FROM user_site_route WHERE uuid='{user_site_route_uuid}'"""

        user_site_route = await self.connection.get_one(statement)

        print(user_site_route)

        page = requests.get("https://getcomposer.org/download/")

        #page = requests.get(user_site_route[0])

        soup = BeautifulSoup(page.content, "html.parser")

        all_elements = []

        elements_by_id = soup.find_all(id=True)
        all_elements.extend(elements_by_id)

        elements_by_class = soup.find_all(class_=True)
        all_elements.extend(elements_by_class)

        elements_list = [{
                "tag": element.name,
                "id": element.get('id'),
                "class": element.get('class')
            } for element in all_elements]
        
        # Exibir a lista de elementos encontrados
        for element in elements_list:
            print(element)

        return {}
    
    async def fine_tunning_by_site(self, user_site_uuid: str) -> object:
        statement = f"""
            SELECT  origin.content, generated.content, generated.tool_call
            FROM chat_message_origin_and_generate cmog
            JOIN chat_message origin ON origin.UUID = cmog.origin_uuid
            JOIN chat_message generated ON generated.uuid = cmog.generate_uuid
            JOIN chat c ON c.uuid = origin.chat_uuid
            JOIN user_site us ON us.uuid = c.user_site_uuid
            WHERE us.uuid = '{user_site_uuid}'
        """

        chat_messages_relations = await self.connection.get(statement)

        mapped_items = np.array([{
            "origin": item[0],
            "generate": {
                "content": item[1],
                "tool_call": item[2]
            }
        } for item in chat_messages_relations])

        print(mapped_items)

        return {}