from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# PostgreSQL connection string
# You can modify these values according to your PostgreSQL setup
DATABASE_URL = settings.database_url

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


