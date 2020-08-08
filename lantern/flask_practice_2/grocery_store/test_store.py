import inject
from fake_storage import FakeStorage
from store_app import app


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Rostyslav Bilan'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_users(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_users(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_successful_update_users(self):
        resp = self.client.post('/users', json={'name': 'John Doe'})
        user_id = resp.json['user_id']
        resp = self.client.put(f'/users/{user_id}', json={'name': 'Rostyslav Bilan'})
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_update_unexistent_users(self):
        resp = self.client.put(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):

    def test_create_new_goods(self):
        resp = self.client.post(
            '/goods',
            json=[
                {
                    'name': 'Chocolate_bar',
                    'price': 10
                },
                {
                    'name': 'Tea',
                    'price': 5
                }
            ]
        )
        assert resp.status_code == 201
        assert resp.json == {'number of items created': 2}

    def test_all_goods(self):
        resp = self.client.post(
            '/goods',
            json=[
                {
                    'name': 'Chocolate_bar',
                    'price': 10
                },
                {
                    'name': 'Tea',
                    'price': 5
                }
            ]
        )
        count_goods = resp.json['number of items created']
        resp = self.client.get('/goods')
        assert resp.status_code == 200
        assert len(resp.json) == count_goods

        goods = [
            {
                'name': 'Chocolate_bar',
                'price': 10
            },
            {
                'name': 'Tea',
                'price': 5
            }
        ]
        excepted_goods = [
            {
                'name': good['name'],
                'price': good['price'],
                'id': id_goods
            }
            for id_goods, good in enumerate(goods, start=1)
        ]
        assert resp.json == excepted_goods

    def test_update_many_goods(self):
        resp = self.client.post(
            '/goods',
            json=[
                {
                    'name': 'Chockolate bar',
                    'price': 10
                },
                {
                    'name': 'Banana',
                    'price': 20
                }
            ]
        )

        resp = self.client.put(
            '/goods',
            json=[
                {
                    'id': 1,
                    'name': 'Apple',
                    'price': 100
                },
                {
                    'id': 2,
                    'name': 'Cookies',
                    'price': 200
                }
            ]
        )
        assert resp.status_code == 200
        assert resp.json == {'successfully_updated': 2}


class TestStores(Initializer):
    def initial_user_data(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        return resp

    def initial_store_data(self, user_id):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}
        )
        return resp

    def test_create_new_store(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        resp = self.initial_store_data(user_id)
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

    def test_create_new_store_with_wrong_manager(self):
        self.initial_user_data()
        resp = self.initial_store_data(user_id=2)
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 2'}

    def test_get_store_by_id(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        self.initial_store_data(user_id)
        resp = self.client.get(f'store/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}

    def test_get_store_by_bad_id(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        self.initial_store_data(2)
        resp = self.client.get(f'/store/{user_id + 1}')
        assert resp.status_code == 404
        assert resp.json == {'error': f'No such store_id {user_id + 1}'}

    def test_update_store(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        self.initial_store_data(user_id)
        resp = self.client.put(
            f'/store/{user_id}',
            json={'name': 'Rostyslav Bilan', 'location': 'Lviv', 'manager_id': user_id}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_update_store_bad_id(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        self.initial_store_data(user_id)
        resp = self.client.put(
            '/store/2',
            json={'name': 'Rostyslav Bilan', 'location': 'Lviv', 'manager_id': user_id}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': f'No such store_id {user_id + 1}'}