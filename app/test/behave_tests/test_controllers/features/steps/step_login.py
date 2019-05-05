from json import loads

from behave import when, then, given
from requests import post

from app.models.user import User
from app.settings.database_settings import session


@given(u'que o usuário {nickname} não exista')
def check_user_not_exists(context, nickname):
    user = session.query(User).filter_by(nickname=nickname).one_or_none()
    assert not user


@given(u'que o usuário {nickname} exista')
def check_user_exists(context, nickname):
    user = session.query(User).filter_by(nickname=nickname).one_or_none()
    assert user.nickname == nickname


@when(u'fazer um login no sistema')
def request_url(context):
    data = loads(context.text)
    context.response = post(url=context.base_url, data=data)


@then(u'a resposta deve ser')
def check_response(context):
    assert context.response.json() == loads(context.text)
