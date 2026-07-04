from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="A privacy-first AI companion that remembers, understands, and grows with one person over time.",
)


@app.on_event("startup")
async def startup():
    logger.info("Starting AGAM...")


@app.get("/")
async def root():
    return {
        "project": settings.APP_NAME,
        "status": "alive",
        "version": settings.VERSION,
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }
