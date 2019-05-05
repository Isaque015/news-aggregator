from bottle import static_file

from app import app


@app.route('/node_modules/<filename:path>')
def node_modules(filename):
    return static_file(filename, root='app/node_modules/')


@app.route('/static_css/<filename:path>')
def stylesheets(filename):
    return static_file(filename, root='app/assets/css')


@app.route('/static_js/<filename:path>')
def static_js(filename):
    return static_file(filename, root='app/assets/js')


@app.route('/images/<filename>')
def images_serve(filename):
    return static_file(filename, root='app/assets/img')
