import logging
from datetime import datetime

from fastapi import Request

logger = logging.getLogger(__name__)


async def request_profiler(request: Request, call_next) -> Request:
    start = datetime.now().astimezone()

    response = await call_next(request)

    elapsed = datetime.now().astimezone() - start
    elapsed_ms = elapsed.total_seconds() * 1000
    logger.info(f'Time elapsed: {elapsed_ms:.2f}ms for {request.method} {request.url}')
    
    return response
