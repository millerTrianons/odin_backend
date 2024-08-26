import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from application.views import RoutingFactory
from infrastructure.error_handling import ErrorHandling

API_TITLE = "Odin"
API_VERSION = "0.0.1"
API_DESCRIPTION = "Advanced Machine Learning Service"

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
    debug=True if os.getenv('DEBUG', None) == '1' else False
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware)

ErrorHandling.create(app)

RoutingFactory.create(app)

