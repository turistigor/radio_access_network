from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql+asyncpg://postgres:ran_password@localhost:5432/ran'
db_engine = create_async_engine(db_url, echo=True, future=True)
session_maker = sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session
