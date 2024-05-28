#!/usr/bin/python3
"""Reviews api for all default RESTFul API actions"""

from api.v1.views import app_views
from models.review import Review
from flask import jsonify, request, abort
from models import storage
from models.place import Place


@app_views.route('/places/<place_id>/reviews',
                 methods=["GET"], strict_slashes=False)
def get_place_r(place_id):
    """returns a review by place_id"""
    place = storage.get(Place, place_id)
    if place is None of place_id is None:
        abort(404)
    rev = storage.all(Review)
    lis = []
    for v in rev.values():
        if v.place_id == place_id:
            lis.append(v)
    return jsonfy(lis.to_dict), 200


@app_views.route("/reviews/<review_id>",
                 methods=["GET"], strict_slashes=False)
def get_rev(review_id):
    """return a review or 404 if not found"""
    rev = storage.get(Review, review_id)
    if rev is None:
        abort(404)

    return jsonify(rev.to_dict()), 200


@app_views.route("/reviews/<review_id>",
                 methods=["GET"], strict_slashes=False)
def del_rev(review_id):
    """deletes a review"""
    rev = storage.get(Review, review_id)
    if rev is None:
        abort(404)

    storage.delete(rev)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def create_rev(place_id):
    """creates a new review"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    header = request.headers.get('Content-Type')
    if header != "application/json":
        return jsonify({'error': 'Not a JSON'}), 400

    resp = request.get_json()
    if resp in None:
        return jsonify({'error': 'Not a JSON'}), 400

    if 'user_id' not in resp.keys():
        return jsonify('error': 'Missing user_id'), 400

    user = storage.get(User, resp['user_id'])
    if user is None:
        abort(404)

    if 'text' not in resp.keys():
        return jsonify({'error': 'Missing text'}), 400

    rev = Review('user_id'=resp['user_id'], 'text'=resp['text'],
                 'place_id'=place_id)
    storage.new(rev)
    storage.save()
    return jsonify(rev.to_dict()), 201


@app_views.route('/reviews/<review_id>',
                 methods=['PUT'], strict_slashes=False)
def update_rev(review_id):
    """updates the review"""
    rev = storage.get(Review, review_id)
    if rev is None:
        abort(404)

    resp = request.get_json()
    if resp is None:
        return jsonify({'error': 'Not a JSON'}), 400
    header = request.headers.get('Content-Type')
    if header != "application/json":
        return jsonify({'error': 'Not a JSON'})

    for k, v in resp.items():
        if k not in ["id", "user_id", "place_id",
                     "created_at", "updated_at"]:
            rev[k] = v
#    storage.
    storage.save()

    return jsonify(rev.to_dict()), 200
