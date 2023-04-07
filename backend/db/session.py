from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import settings
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(settings.POSTGRES_DB_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()