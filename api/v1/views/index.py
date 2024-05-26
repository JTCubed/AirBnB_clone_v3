#!/usr/bin/python3
"""index file for the app"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """returns the status"""
    status = {'status': 'OK'}
    return jsonify(status)
