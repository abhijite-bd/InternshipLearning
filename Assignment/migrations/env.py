import asyncio
from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection
from app.database import Base  # Import Base from your database.py
from app.config import DATABASE_URL  # Import your DATABASE_URL

connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)
async def run_migrations_online():
    """Run migrations in 'online' mode using an async connection."""
    async with connectable.connect() as connection:
        await connection.run_sync(lambda conn: context.configure(
            connection=conn,
            target_metadata=Base.metadata
        ))

        with context.begin_transaction():
            await connection.run_sync(context.run_migrations)

def run_migrations():
    """Run the migrations synchronously by running the async function in an event loop."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_migrations_online())

if context.is_offline_mode():
    context.configure(
        url=DATABASE_URL,
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()
else:
    run_migrations()