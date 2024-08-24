from abc import ABC, abstractmethod
from fastapi import UploadFile, File

class AIManagerRepository:

    @abstractmethod
    async def list_ais(self, user_id: str, offset: int = 0, quantity: int = 10) -> list[object]:
        raise NotImplementedError()
    
    @abstractmethod
    async def train_ai(self, api_key: str, file: UploadFile = File(...)):
        raise NotImplementedError()
    
    @abstractmethod
    async def scrap_user_site_route(self, user_site_route_uuid: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def fine_tunning_by_site(self, user_site_uuid: str) -> object:
        raise NotImplementedError()