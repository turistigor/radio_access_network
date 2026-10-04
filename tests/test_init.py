import asyncio as aio
from datetime import datetime


async def test_init():
    start = datetime.now().astimezone()

    await aio.sleep(1)

    assert start != datetime.now().astimezone()
