from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from infrastructure.failures import Failure


class ErrorHandling:

    @classmethod
    def _json_error_response(cls, error: Exception) -> dict:
        try:

            class_name: str = (
                error.__class__.__module__
                + '.'
                + error.__class__.__name__
            )

        except Exception:
            class_name = str(error.__class__)

        return {
            "error": True,
            "message": str(error),
            # "origin": "",
            "type": class_name
        }

    @classmethod
    def create(cls, app: FastAPI) -> None:
        """Configure generic and specific error handling for all the 
        application.
        """

        @app.exception_handler(Exception)
        async def handle_not_expected_exception(
                request: Request, exception: Exception):
            """All not expected errors handling"""

            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=ErrorHandling._json_error_response(exception)
            )

        @app.exception_handler(ValueError)
        async def handle_validation_error(
                request: Request, exception: ValueError):
            """Validation errors handling"""

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=ErrorHandling._json_error_response(exception)
            )

        @app.exception_handler(Failure)
        async def handle_generic_failures(
                request: Request, exception: Failure):
            """business rules errors handling"""
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=ErrorHandling._json_error_response(exception))

