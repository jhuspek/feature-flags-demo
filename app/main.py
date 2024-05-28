from fastapi import FastAPI

from app.featureflags.manager import unleash_manager
from app.routers.api import router
from app.config import AppProperties

import uvicorn
import logging

config = AppProperties()
application = FastAPI()

application.include_router(router, prefix=config.API_PREFIX)

try:
    unleash_manager.unleash.initialize_client()
except Exception as e:
    logging.error(f"Exception occurred while connecting to Unleash server: {e}")

if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8080)
