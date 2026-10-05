import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from src.endpoints.healthcheck import health_router
from src.middleware.request_timer import request_timer

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


if __name__ == '__main__':

    app = FastAPI(
        title='Radio Access Network',
        openapi_url='/api/v1/openapi',
        docs_url='/api/v1/swagger',
    )

    app.include_router(health_router)
    app.add_middleware(BaseHTTPMiddleware, dispatch=request_timer)

    uvicorn.run(app)
