from sqlalchemy import (Column, Integer, String, PrimaryKeyConstraint,
                        UniqueConstraint)

from argon2 import PasswordHasher

from app.settings.engine_database import Base, engine
from app.settings.session_sql import session
from app.utils.email import tratar_email
from app.utils.get_errors_exceptions import GetErrorException


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(160), nullable=False, unique=True)
    nickname = Column(String(80), nullable=False, unique=True)
    passwd = Column(String(160), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_user_id'),
        UniqueConstraint('email', name='unique_email_user'),
        UniqueConstraint('nickname', name='unique_nickname_user')
    )

    def __repr__(self):
        return f'{self.nickname}'

    def encrypting_password(self):
        if not self.passwd:
            return {'status': False, 'msg': 'senha esta vazia'}

        password_hash = PasswordHasher()
        self.passwd = password_hash.hash(self.passwd)
        return {'status': True, 'msg': 'senha encripitada'}

    def verificar_senha(self, passwd):
        ph = PasswordHasher()
        try:
            ph.verify(self.passwd, passwd)
            return {'status': True, 'msg': 'senha correta'}
        except Exception:
            return {'status': False, 'msg': 'senha incorreta'}

    @tratar_email
    def normalize_email(self, resposta_email_decorator=None):
        return resposta_email_decorator

    def set_attributes(self, **fields):
        for attribute, value in fields.items():
            if value:
                setattr(self, attribute, value)

    def save(self):

        result_encrypting_passwd = self.encrypting_password()
        if not result_encrypting_passwd['status']:
            return result_encrypting_passwd

        result_normalize_email = self.normalize_email()
        if not result_normalize_email['status']:
            return result_normalize_email['msg']

        try:
            session.add(self)
            session.commit()
            return {'status': True, 'msg': 'user save success'}
        except Exception as e:
            erro = str(e.__dict__['orig'])
            get_errors = GetErrorException()
            msg = get_errors.despacho_func(erro)
            return {'status': False, 'msg': msg}
        finally:
            session.close()


Base.metadata.create_all(engine)
