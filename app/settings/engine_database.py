from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://bottle:bottle@psql:5432/bottle')

Base = declarative_base()
