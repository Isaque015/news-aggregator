from sqlalchemy.orm import sessionmaker

from app.settings.engine_database import engine

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
