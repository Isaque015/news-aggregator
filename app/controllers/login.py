from json import dumps, loads

from bottle import (TEMPLATE_PATH, jinja2_template as template, request)

from app import app
from app.models.user import User
from app.settings.database_settings import session as session_postgres

TEMPLATE_PATH.append('app/templates')


@app.route('/')
def index(session, rdb):
    x = session.get('nickname')
    return f'<p> Ola Mundo {x}</p>'


@app.route('/login')
def login():
    return template('login.html.j2')


@app.route('/sign_in', method='POST')
def sign_in(session, rdb):
    nickname = request.json['nickname']
    password = request.json['password']

    if not nickname:
        response = {
            "code": 401,
            "msg": "the nickname field can not be empty",
            "status": False
        }
        return dumps(response)

    if not password:
        response = {
            "code": 401,
            "msg": "the password field can not be empty",
            "status": False
        }
        return dumps(response)

    user = session_postgres.query(User).filter_by(
        nickname=nickname
    ).one_or_none()

    if not user:
        response = {
            "code": 404,
            "msg": "User not found",
            "status": False
        }
        return dumps(response)

    if not user.verificar_senha(password)['status']:
        response = {
            "code": 404,
            "msg": "Wrong password",
            "status": False
        }
        return dumps(response)

    session['nickname'] = user.nickname

    response = {
        "code": 200,
        "msg": "User has been logged in",
        "status": True
    }
    return dumps(response)
