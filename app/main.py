from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("FastAPI starting up")
    yield
    logger.info("FastAPI shutting down")

app = FastAPI(
    title="Languarum FastApi",
    version="0.0.1",
    lifespan=lifespan
)

@app.get("/")
def read_root():
    return {"Hello": "World!"}
