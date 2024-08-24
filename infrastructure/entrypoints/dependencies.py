# pylint: disable=missing-function-docstring
"""Module to configure the custom dependencies for de application
"""

from fastapi import Depends

from data.data_sources.eva_data_souce_impl import EvaDataSourceImpl
from data.services.sql_connection_service import SqlConnectionService

from data.data_sources.chat_data_source_impl import (
    ChatDataSource, ChatDataSourceImpl
)

from data.data_sources.management_data_source_impl import (
    ManagementDataSource, ManagementeDataSourceImpl
)

from data.data_sources.ai_manager_data_source_impl import (
    AIManagerDatasource, AIManagerDataSourceImpl
)

from data.data_sources.auth_data_source_impl import (
    AuthDataSource, AuthDataSourceImpl
)

from data.data_sources.administrator_data_source_impl import (
    AdministratorDataSource, AdministratorDataSourceImpl
)

from data.data_sources.external_apis_data_source_impl import(
    ExternalApisDataSource, ExternalApisDataSourceImpl
)

from domain.repositories.eva_repository import EvaRepository
from infrastructure.data_sources.eva_data_source import EvaDataSource
from infrastructure.repositories.chat_repository_impl import (
    ChatRepository, ChatRepositoryImpl
)

from infrastructure.repositories.eva_repository_impl import EvaRepositoryImpl
from infrastructure.repositories.management_repository_impl import (
    ManagementRepository, ManagementRepositoryImpl
)

from infrastructure.repositories.ai_manager_repository_impl import (
    AIManagerRepository, AIManagerRepositoryImpl
)

from infrastructure.repositories.external_api_repository_impl import (
    ExternalApisRepository, ExternalApiRepositoryImpl
)

from infrastructure.repositories.auth_repository_impl import (
    AuthRepository, AuthRepositoryImpl
)

from infrastructure.repositories.administrator_repository_impl import (
    AdministratorRepository, AdministratorRepositoryImpl
)

from usecases.external_apis_usecase import ExternalApisUsecase

from usecases.chat_usecase import ChatUsecase

from usecases.auth_usecase import AuthUsecase

from usecases.ai_manager_usecase import AIManagerUsecase

from usecases.management_usecase import ManagementUseCase

from usecases.adminstrator_usecase import AdministratorUsecase

from usecases.eva_usecase import EvaUseCase

def get_chat_repository(
        data_source: ChatDataSource = Depends(ChatDataSourceImpl),
) -> ChatRepository:
    return ChatRepositoryImpl(data_source)

def get_auth_repository(
        data_source: AuthDataSource = Depends(AuthDataSourceImpl)
) -> AuthRepository:
    return AuthRepositoryImpl(data_source)

def get_ai_manager_repository(
        data_source: AIManagerDatasource = Depends(AIManagerDataSourceImpl)
) -> AIManagerRepository:
    return AIManagerRepositoryImpl(data_source)

def get_management_repository(
        data_source: ManagementDataSource = Depends(ManagementeDataSourceImpl)
) -> ManagementRepository:
    return ManagementRepositoryImpl(data_source)

def get_administrator_repository(
        data_source: AdministratorDataSource = Depends(AdministratorDataSourceImpl)
) -> AdministratorRepository:
    return AdministratorRepositoryImpl(data_source)

def get_external_apis_repository(
        data_source: ExternalApisDataSource = Depends(ExternalApisDataSourceImpl)
) -> ExternalApisRepository:
    return ExternalApiRepositoryImpl(data_source)

def get_eva_repository(
        data_source: EvaDataSource = Depends(EvaDataSourceImpl)
) -> EvaRepository:
    return EvaRepositoryImpl(data_source)

def get_chat_usecase(
        repo: ChatRepository = Depends(get_chat_repository)
) -> ChatUsecase:
    return ChatUsecase(repo)

def get_auth_usecase(
        repo: AuthRepository = Depends(get_auth_repository)
) -> AuthUsecase:
    return AuthUsecase(repo)

def get_ai_manager_usecase(
        repo: AIManagerRepository = Depends(get_ai_manager_repository)
) -> AIManagerUsecase:
    return AIManagerUsecase(repo)

def get_management_usecase(
        repo: ManagementRepository = Depends(get_management_repository)
) -> ManagementUseCase:
    return ManagementUseCase(repo)

def get_administrator_usecase(
        repo: AdministratorRepository = Depends(get_administrator_repository)
) -> AdministratorUsecase:
    return AdministratorUsecase(repo)

def get_external_apis_usecase(
        repo: ExternalApisRepository = Depends(get_external_apis_repository)
) -> ExternalApisUsecase:
    return ExternalApisUsecase(repo)

def get_eva_usecase(
        repo: EvaRepository = Depends(get_eva_repository)
) -> EvaUseCase:
    return EvaUseCase(repo)


