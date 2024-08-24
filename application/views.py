from fastapi import FastAPI

from infrastructure.entrypoints.chat_entrypoints import \
    router as chat_router

from infrastructure.entrypoints.auth_entrypoints import \
    router as auth_router

from infrastructure.entrypoints.ai_manager_entrypoints import \
    router as ai_manager_router

from infrastructure.entrypoints.management_entrypoints import \
    router as management_router

from infrastructure.entrypoints.administrator_entrypoints import \
    router as adminstrator_route

from infrastructure.entrypoints.external_apis_entrypoints import \
    router as external_apis_access_route

from infrastructure.entrypoints.eva_entrypoints import \
    router as eva_router


class RoutingFactory:

    @staticmethod
    def create(app: FastAPI):

        app.include_router(
            chat_router,
            prefix='/chat',
            tags=['chat']
        )

        app.include_router(
            auth_router,
            prefix='/auth',
            tags=['auth']
        )

        app.include_router(
            ai_manager_router,
            prefix='/ai_manager',
            tags=['ai_manager']
        )

        app.include_router(
            management_router,
            prefix='/management',
            tags=['management']
        )

        app.include_router(
            adminstrator_route,
            prefix='/administrator',
            tags=['administrator']
        )

        app.include_router(
            external_apis_access_route,
            prefix='/api_access',
            tags=['api_access']
        )

        app.include_router(
            eva_router,
            prefix='/eva',
            tags=['eva']
        )

        

        
