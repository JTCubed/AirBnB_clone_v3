#!/usr/bin/python3
"""api for Airbnb"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage."""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """return json error: not found"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    if getenv('HBNB_API_HOST', '0.0.0.0'):
        host1 = getenv('HBNB_API_HOST')
    else:
        host1 = '0.0.0.0'
    if getenv('HBNB_API_PORT'):
        port1 = int(getenv('HBNB_API_PORT'))
    else:
        port1 = 5000

    app.run(host=host1, port=port1, threaded=True)
