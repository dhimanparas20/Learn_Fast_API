from fastapi import FastAPI, Request
import time
from loguru import logger

async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url} - {duration:.4f}s")
    return response
