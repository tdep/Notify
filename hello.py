from flask import Flask

app = Flask("Notify")

@app.route('/')
def hello():
    return f'Wello Horld!!'