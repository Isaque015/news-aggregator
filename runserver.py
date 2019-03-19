import bottle

from app import app

if __name__ == '__main__':
    try:
        from os import environ

        if environ['RUN_GUNICORN']:
            app_gunicorn = bottle.default_app()
    except KeyError:
        app.run(host='0.0.0.0', port=8080)
