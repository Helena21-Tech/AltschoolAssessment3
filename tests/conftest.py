from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker, AsyncSession
)
from sqlalchemy.pool import NullPool
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.core.db_async import Base
from app.core.deps import get_async_db
from app.main import app
from app.core.config import settings
# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.errors import RateLimitExceeded


DATABASE_URL = settings.TEST_DATABASE_URL_ASYNC 
print("DATABASE_URL:", repr(DATABASE_URL))
engine = create_async_engine(DATABASE_URL, poolclass=NullPool)

TestingSessionLocal = async_sessionmaker(
    bind=engine,
    class_= AsyncSession,
    expire_on_commit=False
)


@pytest_asyncio.fixture(scope="session", autouse=True)   
async def setup_database():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)



@pytest_asyncio.fixture(autouse=True)
async def override_dependencies():
   
    async def override_get_db():
        async with TestingSessionLocal() as session:
            yield session
            await session.rollback()

    app.dependency_overrides[get_async_db] = override_get_db
    yield
    app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def client():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as ac:
        yield ac







