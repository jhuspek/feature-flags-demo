from fastapi import FastAPI
from app.routers.api import router
from app.config import AppProperties
from app.featureflags.manager import unleash_manager
import uvicorn
import asyncio
import logging
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)

config = AppProperties()


@asynccontextmanager
async def lifespan(app: FastAPI):
    retry_interval = 30

    while not unleash_manager.connected:
        try:
            logging.info("Attempting to connect to Unleash server...")
            unleash_manager.initialize()
            if unleash_manager.connected:
                logging.info("Successfully connected to Unleash server.")
                break
        except Exception as e:
            logging.error(f"Exception occurred while connecting to Unleash server: {e}")

        logging.info(f"Retrying in {retry_interval} seconds...")
        await asyncio.sleep(retry_interval)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router, prefix=config.API_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
