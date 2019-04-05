from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bottle.ext import sqlalchemy as bottle_sqlalchemy

from app.models import Base
from app.settings import default_config

engine = create_engine(default_config['db_url'])

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

sqlalchemy_plugin = bottle_sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)
