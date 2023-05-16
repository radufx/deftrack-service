from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASS = os.getenv("POSTGRES_PASS")
POSTGRES_DATABASE_NAME = os.getenv("POSTGRES_DATABASE_NAME")

engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@localhost/{POSTGRES_DATABASE_NAME}", echo=True)

Base = declarative_base()

LocalSession = sessionmaker(bind=engine)
db = LocalSession()
