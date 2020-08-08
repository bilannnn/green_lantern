import inject
from fake_storage import FakeStorage
from store_app import app
from views import users_bp, goods_bp, store_bp


def configure(binder):
    db = FakeStorage()
    binder.bind('DB', db)


inject.clear_and_configure(configure)

if __name__ == '__main__':
    app.register_blueprint(users_bp)
    app.register_blueprint(goods_bp)
    app.register_blueprint(store_bp)

    app.run(port=8080, debug=True)
