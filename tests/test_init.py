import asyncio as aio
from datetime import datetime


async def test_init():
    start = datetime.now()

    await aio.sleep(1)

    assert start != datetime.now()
