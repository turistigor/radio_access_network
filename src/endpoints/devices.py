from datetime import datetime
import logging

from fastapi import APIRouter, Depends
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.devices import DeviceChangeStatus
from src.db.api import get_db
from src.db.models import DeviceModel

logger = logging.getLogger(__name__)
devices_router = APIRouter(prefix='/api/v1')


@devices_router.patch('/device/{device_id}')
async def change_status(
    device_id: int, payload: DeviceChangeStatus, db: AsyncSession=Depends(get_db)
) -> dict:
    logger.info(f'{device_id=} {payload.status=}')

    async with db.begin():
        query = (
            update(DeviceModel)
            .where(DeviceModel.id == device_id)
            .values(
                status=payload.status, 
                last_updated=datetime.now().astimezone()
            )
        )
        result = await db.execute(query)

    logger.info(result)

    return {}
