from sqlalchemy import Column, Integer, String
from argon2 import PasswordHasher

from app.settings.engine_database import Base, engine
from app.settings.session_sql import session


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    last_name = Column(String(80))
    email = Column(String(160))
    nickname = Column(String(80))
    passwd = Column(String(160))

    def __repr__(self):
        return f'User(name="{self.name}", \
                full_name="{self.name} {self.last_name}",\
                nickname="{self.nickname}")'

    def generate_password(self, passwd):
        ph = PasswordHasher()
        hash = ph.hash(passwd)
        return hash

    def set_attributes(self, **fields):

        if not fields.get('passwd'):
            raise AttributeError('password not found')

        if not fields.get('email'):
            raise AttributeError('password not found')

        self.passwd = self.generate_password(fields.get('passwd'))

        for attribute, value in fields.items():
            if attribute == 'passwd':
                continue

            setattr(self, attribute, value)

    def save(self, **fields):
        self.set_attributes(self, **fields)

        session.add(self)
        session.commit()
        session.close()


Base.metadata.create_all(engine)
