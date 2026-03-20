from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings

# Quitar query parameters incompatibles con asyncpg
db_url = settings.DATABASE_URL.split("?")[0]

engine = create_async_engine(
    db_url,
    echo=False,
    connect_args={"ssl": True}
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
