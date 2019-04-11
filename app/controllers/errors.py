from bottle import jinja2_view

from app import app


@app.error(404)
@jinja2_view('app/templates/error404.html')
def error404(error):
    return


@app.error(500)
def error500(error):
    return 'Nothing here 500, sorry'
