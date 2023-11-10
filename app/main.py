from fastapi import FastAPI

from app.featureflags.manager import unleash_manager
from app.routers.api import router
from app.config import AppProperties

import uvicorn

config = AppProperties()


def init_application() -> FastAPI:
    application = FastAPI()

    application.include_router(router, prefix=config.API_PREFIX)

    unleash_manager.unleash.initialize_client()

    uvicorn.run(application, host="0.0.0.0", port=8080)

    return application


app = init_application()
