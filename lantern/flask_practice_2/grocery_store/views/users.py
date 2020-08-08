import inject
from fake_storage import FakeStorage
from flask import Flask, jsonify, request, Blueprint

users_bp = Blueprint('users', __name__)

app = Flask(__name__)
app.register_blueprint(users_bp)


@users_bp.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db: FakeStorage = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'})
