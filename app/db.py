# app/db.py

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Voor Oracle: cx_Oracle://user:password@host:port/?service_name=XXX
DATABASE_URL = "sqlite:///./retail.db"  # voor testen lokaal
# DATABASE_URL = "oracle+cx_oracle://user:password@host:port/?service_name=XXX"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
