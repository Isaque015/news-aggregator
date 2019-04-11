from bottle import Bottle

app = Bottle()

# controllers
from app.controllers import login
from app.controllers import errors

# models
from app.models import user
from app.models import base_model

# settings
from app.settings import database_settings
from app.settings import setup_log

#utils
from app.utils import email
