# from core import app
from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Jorb",
        "lastname": "Jorberson"
    }

    return response_body

