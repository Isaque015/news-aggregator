from app import app
from app.settings.database_settings import sqlalchemy_plugin
from app.settings import default_config

app.install(sqlalchemy_plugin)
APP_GUNICORN = app

if __name__ == '__main__':
    app.run(
        host=default_config['host'],
        port=default_config['port'],
        debug=default_config['debug'],
        reloader=default_config['reloader']
    )
