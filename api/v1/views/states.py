#!/usr/bin/python3
"""views for the State class"""

from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
@app_views.route('/states/', methods=['GET'])
@app_views.route('/states/<state_id>', methods=['GET', 'DELETE'])
def states_cls(state_id=None):
    """
    returns all state instances,
    a single state instance by if,
    404 if not found
    """
    dict = {}

    if state_id:
        state = storage.get(State, state_id)
        try:
            js = state.to_dict()
            return jsonify(js)
        except Exception:
            abort(404)

    else:
        all_state = storage.all(State)
        ls = []
#        params = ["__class__", "created_at", ]
        for k in all_state.values():
            state_dict = k.to_dict()
            ls.append(state_dict)
        return jsonify(ls)
