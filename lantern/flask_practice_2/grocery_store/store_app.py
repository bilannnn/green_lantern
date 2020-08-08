from errors import NoSuchUserError, NoSuchStoreError
from flask import Flask, jsonify

app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchStoreError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404

