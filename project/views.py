from flask import jsonify
from datetime import date
from project import app

@app.route("/")
def homepage():
    response = "<h1>Hello World!</h1>"
    return response, 200

@app.route("/healthcheck")
def healthCheck():
    response = {
        'time': str(date.today()),
        'status': 200,
    }
    return jsonify(response), 200
