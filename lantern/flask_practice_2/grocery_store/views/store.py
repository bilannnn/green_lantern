import inject
from flask import Flask, jsonify, request, Blueprint
from fake_storage import FakeStorage


store_bp = Blueprint('store', __name__)

app = Flask(__name__)
app.register_blueprint(store_bp)


@store_bp.route('/store', methods=['POST'])
def create_new_store():
    db: FakeStorage = inject.instance('DB')
    db.users.get_user_by_id(request.json['manager_id'])
    store_id = db.stores.add(request.json)
    return jsonify({'store_id': store_id}), 201


@store_bp.route('/store/<int:store_id>')
def get_store(store_id):
    db: FakeStorage = inject.instance('DB')
    store = db.stores.get_store_by_id(store_id)
    return jsonify(store)


@store_bp.route('/store/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    db: FakeStorage = inject.instance('DB')
    db.users.get_user_by_id(request.json['manager_id'])
    db.stores.update_store_by_id(store_id, request.json)
    return jsonify({'status': 'success'})
