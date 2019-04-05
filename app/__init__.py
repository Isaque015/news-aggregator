from bottle import Bottle

app = Bottle()

# controllers
from app.controllers import login

# models
from app.models import user

# settings
from app.settings import database_settings
