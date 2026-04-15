# main.py
import logging
from fastapi import FastAPI
from api.v1.endpoints import router
import uvicorn
from core.config import settings

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="FastAPI Secure Egress Proxy",
    description="A secure reverse proxy service with API key authentication and domain allowlist.",
    version="1.0.0",
    docs_url="/docs",
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True)