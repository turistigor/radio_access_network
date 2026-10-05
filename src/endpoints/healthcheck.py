from fastapi import APIRouter, Request
import starlette.status as st

health_router = APIRouter(prefix='/api/v1')

@health_router.get('/health')
async def healthcheck(request: Request) -> dict:
    return {'status': st.HTTP_200_OK}
