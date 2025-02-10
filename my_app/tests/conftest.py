import asyncio
import httpx
import pytest
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from my_app.config import DB_USER, DB_HOST, DB_PORT, DB_NAME_TEST, DB_PASS
from my_app.database import Base
from my_app.dependencies import get_async_session
from my_app.main import app


DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=pool.NullPool, echo=True)
# NullPool для тестов можно, для продакшена нельзя.
TestSessionLocal = async_sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)

metadata = Base.metadata


async def override_get_async_session():
    async with TestSessionLocal() as session:
        yield session
        # Откатываем транзакции после теста
        await session.rollback()


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def db_session():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope="session")
async def aclient():
    async with httpx.AsyncClient(app=app, base_url="http://test") as aclient:
        yield aclient
