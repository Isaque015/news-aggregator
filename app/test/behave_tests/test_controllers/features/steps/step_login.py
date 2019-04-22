from behave import (when, then)
from requests import get


@when(u'fazer um login sem nickname na url "{url}"')
def request_url(context, url):
    context.response = get(url=f'{context.base_url}{url}')


@then(u'a resposta deve ser')
def check_response(context):
    assert context.response == context.text
