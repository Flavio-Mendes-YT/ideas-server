from datetime import datetime
from entity.Idea import Idea
from flask import Flask, request
import jsonpickle

app = Flask(__name__)

@app.route("/ideas")
def get_ideas():
    idea1 = Idea("Ideia test", datetime.now(), False)
    idea2 = Idea("Ideia test 2", datetime.now(), True)
    return jsonpickle.encode([idea1, idea2], unpicklable=False)


@app.route("/idea/<id>", methods=["GET", "POST", "DELETE"])
def idea(id):
    if request.method == 'GET':
        return f'get {id}'
    if request.method == 'POST':
        return f'post {id}'
    if request.method == 'DELETE':
        return f'delete {id}'
