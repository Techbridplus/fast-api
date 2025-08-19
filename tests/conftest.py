import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base, get_db
from app.main import app
from fastapi.testclient import TestClient
from app import models
import os

# Test database URL
SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ.get('DATABASE_USERNAME')}:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_HOSTNAME')}:{os.environ.get('DATABASE_PORT')}/{os.environ.get('DATABASE_NAME')}"

# Create test database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create test session
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def session():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Create a db session
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    # Drop tables after test
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(session):
    # Override the dependency to use the test database
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    
    # Override the get_db dependency
    app.dependency_overrides[get_db] = override_get_db
    
    # Create a test client
    with TestClient(app) as c:
        yield c
    
    # Clean up
    app.dependency_overrides.clear()
