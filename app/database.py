from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import env


SQLALCHEMY_DATABASE_URL = f'postgresql://{env.USER}:{env.PASSWORD}@{env.HOST}:{env.PORT}/LibraryApp'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)

Base = declarative_base()