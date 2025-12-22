import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables from .env file
load_dotenv()

# Base class for our models
Base = declarative_base()

# We'll initialize these globally but defer the actual engine creation to startup
engine = None
AsyncSessionLocal = None

def init_engine():
    """Initialize the database engine with the appropriate connection string."""
    global engine, AsyncSessionLocal

    # Check if Neon database URL is set, otherwise use SQLite for development
    database_url = os.getenv("NEON_DATABASE_URL")
    if not database_url or "localhost" in database_url:
        # Use SQLite for local development if no valid remote URL is provided
        database_url = "sqlite+aiosqlite:///:memory:"
    else:
        # Use the provided database URL (assuming it's a valid PostgreSQL URL)
        pass

    # Create an async engine
    engine = create_async_engine(database_url, echo=False)

    # Create a sessionmaker
    AsyncSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False  # Important for keeping objects detached after commit
    )

@asynccontextmanager
async def get_db():
    """Dependency to get an async database session."""
    if AsyncSessionLocal is None:
        raise RuntimeError("Database engine not initialized. Call init_engine() first.")

    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def init_db():
    """Initializes the database schema."""
    if engine is None:
        raise RuntimeError("Database engine not initialized. Call init_engine() first.")

    async with engine.begin() as conn:
        # This is typically used to create tables for models defined using Base.metadata
        # For Alembic, this might not be directly used, but useful for initial setup or testing.
        await conn.run_sync(Base.metadata.create_all)

# Example usage (for testing connection)
async def check_db_connection():
    try:
        if engine is None:
            raise RuntimeError("Database engine not initialized. Call init_engine() first.")
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        print("Database connection successful!")
        return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False

if __name__ == "__main__":
    import asyncio
    init_engine()
    asyncio.run(init_db())
    asyncio.run(check_db_connection())
