from presentation.user_style_sheet_data import UserStyleSheetData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class UserStyleSheet(SQLModel, table=True):
    __tablename__ = "user_site_style_sheet"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    style_sheet_url: Optional[str]
    style_sheet_name: str
    style_sheet_description: Optional[str]
    style_sheet_content: Optional[str]
    user_site_uuid: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))

    def __init__(
            self,
            uuid: str,
            style_sheet_url: str,
            style_sheet_name: str,
            style_sheet_description: Optional[str],
            style_sheet_content: Optional[str],
            user_site_uuid: str,
        
        ) -> None:
        self.uuid = uuid
        self.style_sheet_url = style_sheet_url
        self.style_sheet_name = style_sheet_name
        self.style_sheet_description = style_sheet_description
        self.style_sheet_content = style_sheet_content
        self.user_site_uuid = user_site_uuid
    
    @staticmethod
    def from_entity(
            user_style_sheet_data: UserStyleSheetData,
            uuid_data: Optional[str]
        ):
        return UserStyleSheet(
            uuid=uuid_data if uuid_data else uuid.uuid4(),
            style_sheet_url=user_style_sheet_data.style_sheet_url,
            style_sheet_name=user_style_sheet_data.style_sheet_name,
            style_sheet_description=user_style_sheet_data.style_sheet_description,
            style_sheet_content=user_style_sheet_data.style_sheet_content,
            user_site_uuid=user_style_sheet_data.user_site_uuid
        )