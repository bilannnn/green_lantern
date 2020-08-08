import inject
from flask import Flask, jsonify, request, Blueprint
from fake_storage import FakeStorage

goods_bp = Blueprint('goods', __name__)

app = Flask(__name__)
app.register_blueprint(goods_bp)


@goods_bp.route('/goods', methods=['POST'])
def create_goods():
    db: FakeStorage = inject.instance('DB')
    count_of_goods_created = db.goods.add(request.json)
    return jsonify({'number of items created': count_of_goods_created}), 201


@goods_bp.route('/goods')
def get_goods():
    db: FakeStorage = inject.instance('DB')
    goods = db.goods.get_all_goods()
    return jsonify(goods)


@goods_bp.route('/goods', methods=['PUT'])
def update_goods():
    db: FakeStorage = inject.instance('DB')
    count_of_updated_goods, error_id_unsuccessful_update = db.goods.update_goods(request.json)
    if error_id_unsuccessful_update:
        return jsonify(
            {
                'successfully_updated': count_of_updated_goods,
                'errors': {
                    'no such id in goods': error_id_unsuccessful_update
                }
            }
        )
    else:
        return jsonify({'successfully_updated': count_of_updated_goods})
