from datetime import datetime
from persistence.initializer import init_db
from entity.idea import Idea
from flask import Flask, request
import jsonpickle
from playhouse.shortcuts import dict_to_model, model_to_dict


app = Flask(__name__)
init_db()

@app.route("/ideas")
def get_ideas():
    ideas = Idea().select().execute()
    return jsonpickle.encode(list(map(model_to_dict, ideas)), unpicklable=False)


@app.route("/idea/<id>", methods=["GET", "PUT", "DELETE"])
def idea(id):
    if request.method == 'GET':
        idea = Idea.select().where(Idea.id == id).get()
        return jsonpickle.encode(model_to_dict(idea), unpicklable=False)
    if request.method == 'PUT':
        idea = dict_to_model(Idea, request.get_json())
        idea.save()
        return request.get_json()
    if request.method == 'DELETE':
        Idea.delete_by_id(id)
        return 'OK'

@app.route("/idea", methods=["POST"])
def create_idea():
    idea = request.get_json()
    saved_idea = Idea.save(dict_to_model(Idea, idea))
    return idea