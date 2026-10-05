import logging

from fastapi import APIRouter

from src.models.devices import DeviceChangeStatus

logger = logging.getLogger(__name__)
devices_router = APIRouter(prefix='/api/v1')


@devices_router.patch('/device/{id}')
async def change_status(id: int, status: DeviceChangeStatus) -> dict:
    logger.info(f'{id=} {status=}')
    return {}
