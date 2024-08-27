from typing import Any, List
import os
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.sql import text

class SqlConnectionService:
    def __init__(self):
        self._engine=create_engine(url=os.environ.get('DB_URL'))
        self._session: Session = None

    async def get_one(self, statement) -> Any:
        """Ready from database and return only the first record"""
        result = None
        with Session(self._engine) as session:
            if isinstance(statement, str):
                results = session.exec(text(statement))
            else:
                results = session.exec(statement)
            result = results.first()
        return result

    async def get(self, statement) -> List[Any]:
        """Ready from database and return the records"""
        result = None
        with Session(self._engine) as session:
            if isinstance(statement, str):
                results = session.exec(text(statement))
            else:
                results = session.exec(statement)
            result = results.all()
        return result

    async def insert(
            self, instances: List[SQLModel], commit: bool = True) -> None:

        if not self._session or not self._session.is_active:
            self._session = Session(self._engine)

        for instance in instances:
            self._session.add(instance)

        if instances and commit:
            self._session.commit()

    async def update(self, statement, commit: bool = True) -> Any:

        if not self._session or not self._session.is_active:
            self._session = Session(self._engine)

        if isinstance(statement, str):
          self._session.exec(text(statement))  
        else:
            self._session.exec(statement)

        if commit:
            self._session.commit()

        return True

    async def commit(self) -> Any:
        if self._session and self._session.in_transaction:
            self._session.commit()

    async def rollback(self) -> Any:
        if self._session and self._session.in_transaction:
            self._session.rollback()

