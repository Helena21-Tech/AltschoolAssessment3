from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from app.core.db_async import AsyncSessionLocal

# Synchronous
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Async
async def get_async_db():
    async with AsyncSessionLocal() as db: #already a context so no need for db.close()
        yield db

