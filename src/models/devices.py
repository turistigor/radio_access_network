from enum import StrEnum

from pydantic import BaseModel


class DeviceStatus(StrEnum):
    active = 'active'
    inactive = 'inactive'


class DeviceChangeStatus(BaseModel):
    status: DeviceStatus

    def __repr__(self) -> str:
        return f'{self.status}'
