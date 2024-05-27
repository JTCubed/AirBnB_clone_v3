#!/usr/bin/python3
"""views for the State class"""

from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State
import json
from flask import request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
# @app_views.route('/states/', methods=['GET'], strict_slashes=False)
def states_cls():
    """
    returns all state instances,
    a single state instance by if,
    404 if not found
    """
    dict = {}

    all_state = storage.all(State)
    ls = []
#   params = ["__class__", "created_at", ]
    for k in all_state.values():
        state_dict = k.to_dict()
        ls.append(state_dict)
    return jsonify(ls)


@app_views.route('/states/<string:state_id>', methods=['GET'])
def get_state(state_id):
    """ Returns a state by Id"""

    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    js = state.to_dict()
    if js is None:
        abort(404)

    return jsonify(js)


@app_views.route('/states/<string:state_id>', methods=['DELETE'])
def delete(state_id):
    """ """
    dict = {}
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return jsonify(dict), 200


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def put_state():
    """ """
    new_state = State()
    data = request.get_json()
    for k, v in data.items():
        setattr(new_state, k, v)
#    if not hasattr(data, 'name'):
#        abort(404)
    return jsonify(new_state.to_dict())
