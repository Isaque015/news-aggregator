from app import app


@app.route('/')
def login():
    return "hello world bottle"
