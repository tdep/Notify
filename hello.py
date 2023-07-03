from flask import Flask

app = Flask("Notify")

@app.route('/')
def hello():
    return f'My first Flask!'