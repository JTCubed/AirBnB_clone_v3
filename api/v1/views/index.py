#!/usr/bin/python3
"""index file for the app"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity


@app_views.route('/status', methods=['GET'])
def status():
    """returns the status"""
    status = {'status': 'OK'}
    return jsonify(status)


@app_views.route('/stats', methods=['GET'])
def num_objects():
    """returns number of each class objects"""
    clas_lis = [Amenity, City, Place, Review, State, User]
    clas_lis_k = ["amenities", "cities", "places", "reviews",
                  "states", "users"]
    j = 0
    dict = {}
    for i in clas_lis:
        dict[clas_lis_k[j]] = storage.count(i)
        j += 1
    return jsonify(dict)
