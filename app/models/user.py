from argon2 import PasswordHasher
from sqlalchemy import (Column, Integer, PrimaryKeyConstraint, String,
                        UniqueConstraint)


from app.models.base_model import BaseModel
from app.models import Base
from app.settings.database_settings import session
from app.utils.email import tratar_email
from app.settings.setup_log import logger


class User(Base, BaseModel):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    last_name = Column(String(80))
    email = Column(String(160), nullable=False)
    nickname = Column(String(80), nullable=False)
    password = Column(String(160), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_user_id'),
        UniqueConstraint('email', name='unique_email_user'),
        UniqueConstraint('nickname', name='unique_nickname_user')
    )

    def __repr__(self):
        return f'{self.nickname}'

    def encrypting_password(self):
        if not self.password:
            return {'status': False, 'msg': 'password not allow blank'}

        password_hash = PasswordHasher()
        self.password = password_hash.hash(self.password)
        return {'status': True, 'msg': 'senha encripitada'}

    def verificar_senha(self, password):
        ph = PasswordHasher()
        try:
            ph.verify(self.password, password)
            return {'status': True, 'msg': 'senha correta'}
        except Exception:
            return {'status': False, 'msg': 'senha incorreta'}

    @tratar_email
    def normalize_email(self, resposta_email_decorator=None):
        return resposta_email_decorator

    def save(self):
        try:
            result_do_not_let_save_empty = self.__do_not_let_save_empty__()
            if not result_do_not_let_save_empty['status']:
                return result_do_not_let_save_empty

            result_verify_attr_exists = self.__verify_attr_exists__()
            if not result_verify_attr_exists['status']:
                return result_verify_attr_exists

            result_encrypting_passwd = self.encrypting_password()
            if not result_encrypting_passwd['status']:
                return result_encrypting_passwd

            result_normalize_email = self.normalize_email()
            if not result_normalize_email['status']:
                return result_normalize_email

            session.add(self)
            session.commit()
            return {'status': True, 'msg': 'user save success'}

        except Exception as e:
            logger.error(e)
            return {'status': False, 'msg': 'Could not save user'}
        finally:
            session.close()
