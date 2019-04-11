from bottle import static_file

from app import app


@app.route('/static/<filename:path>')
def node_modules(filename):
    return static_file(filename, root='app/node_modules/')


@app.route('/static_css/<filename:path>')
def stylesheets(filename):
    return static_file(filename, root='app/assets/css')


@app.route('/images/<filename>')
def images_serve(filename):
    return static_file(filename, root='app/assets/img')
