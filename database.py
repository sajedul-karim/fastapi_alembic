from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:admin@localhost:3309/fastapi_db")
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=3600, connect_args={"ssl": {"ssl_disabled": True}})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
