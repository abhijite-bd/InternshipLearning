import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text 

DATABASE_URL = "postgresql+asyncpg://user:abhijite@localhost:5432/fast_api_database"

async def test_connection():
    try:
        engine = create_async_engine(DATABASE_URL, echo=True)
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))  
        print("Database connection successful!")
    except Exception as e:
        print("Database connection failed:", e)

asyncio.run(test_connection())
