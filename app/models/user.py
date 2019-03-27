from re import match as re_match

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

    def encrypting_password(self):
        password_hash = PasswordHasher()
        self.passwd = password_hash.hash(self.passwd)
        return

    def normalize_email(self):
        result_match_email = re_match(
            r'^([\w\.\-]+)@([\w]+)(\.)(\w*)((\.(\w*))?)$', self.email
        )

        if result_match_email:
            return {'status': True, 'msg': 'Email is valid'}

        if '@' not in self.email:
            return {'status': False, 'msg': 'not @ in email'}

        nick, domain_name = self.email.split('@')

        if not domain_name:
            return {'status': False, 'msg': 'not domain name'}

        if '.' not in domain_name:
            return {'status': False, 'msg': 'not "." in domain name'}
        return {'status': False, 'msg': 'invalid E-mail'}

    def set_attributes(self, **fields):
        for attribute, value in fields.items():
            setattr(self, attribute, value)

    def save(self):

        self.encrypting_password()

        if not self.normalize_email()['status']:
            return self.normalize_email()['msg']

        session.add(self)
        session.commit()
        session.close()


Base.metadata.create_all(engine)
