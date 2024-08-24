from infrastructure.data_sources.administrator_data_source import AdministratorDataSource
from data.services.sql_connection_service import SqlConnectionService

class AdministratorDataSourceImpl(AdministratorDataSource):
    connection: SqlConnectionService

    def __init__(self) -> None:
        self.connection = SqlConnectionService()
    
    async def list_users(self) -> list[object]:
        statement = f"SELECT * from user_"
        
        users = await self.connection.get(statement)

        return [{
            'uuid': user[1], 
            'email': user[2],
            'created_at': user[3]
            } for user in users]
    
    async def list_api_keys(self) -> list[object]:
        statement = f"SELECT * from api_key"
        
        api_keys = await self.connection.get(statement)

        return [{
            'key': api_key[1], 
            'user_id': api_key[2]} for api_key in api_keys]
    
    async def list_messages_relations(self, limit: int) -> list[object]:
        statement = f"SELECT uuid, origin_uuid, generate_uuid, created_at FROM chat_message_origin_and_generate LIMIT {limit}"

        message_relations = await self.connection.get(statement)
        
        return {'data': [{
                'uuid': item[0],
                'origin_uuid': item[1],
                'generate_uuid': item[2],
                'created_at': item[3]
            } for item in message_relations]} 
