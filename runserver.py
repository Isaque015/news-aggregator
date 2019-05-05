from app import app
from app.settings.database_settings import sqlalchemy_plugin
from app.settings import default_config
from app.settings.redis_settings import plugin_session, plugin_redis

app.install(sqlalchemy_plugin)
app.install(plugin_redis)
app.install(plugin_session)

APP_GUNICORN = app

if __name__ == '__main__':
    app.run(
        host=default_config['host'],
        port=default_config['port'],
        debug=default_config['debug'],
        reloader=default_config['reloader']
    )
