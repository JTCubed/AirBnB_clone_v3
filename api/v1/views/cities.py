#!/usr/bin/python3
"""views for the State class"""

from api.v1.views import app_views
from flask import jsonify, abort, make_response
from models import storage
from models.state import State
from models.city import City
import json
from flask import request


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """ Returns a city by Id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_state_by_id(state_id):
    """ Returns a state by Id"""

    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict() for city in state.cities]

    return jsonify(cities)


@app_views.route('/cities/<string:city_id>', methods=['DELETE'])
def delete_city(city_id):
    """deletes a state instance"""
    dict = {}
    state = storage.get(City, city_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify(dict), 200


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """creates a new state and returns it"""
    data = request.get_json(silent=True)
    if data is None:
        return (jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.json:
        return make_response(jsonify({"error": "Missing name"}), 400)
    new_state = City(name=request.json['name'], state_id=state_id)
    data = request.get_json()

    storage.new(new_state)
    storage.save()

    response = make_response(jsonify(new_state.to_dict()), 201)
    response.headers['Content-Type'] = 'application/json'

    return jsonify(new_state.to_dict()), 201


@app_views.route('/cities/<city_id>',
                 methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    if city_id is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    for key, value in request.json.items():
        if key not in ['id', 'state_id',
                       'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict()), 200
