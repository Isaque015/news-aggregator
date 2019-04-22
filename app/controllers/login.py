from bottle import (TEMPLATE_PATH, jinja2_template as template, request)
from wtforms_sqlalchemy.orm import model_form

from app import app
from app.models.user import User

TEMPLATE_PATH.append('app/templates')


@app.route('/login')
def login():
    user_form = model_form(User)
    user = User()

    if request.GET:
        form = user_form(request.forms, obj=user)

        if form.validate():
            form.populate_obj(user)
    else:
        form = user_form(obj=user)

    return template('login.html.j2', dict(form=form))
