from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

DB_HOST = DB_HOST
DB_PORT = DB_PORT
DB_NAME = DB_NAME
DB_USER = DB_USER
DB_PASSWORD = DB_PASSWORD

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)

def get_session():
    session = new_session()
    return session

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    __allow_unmapped__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"