class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


class NoSuchStoreError(Exception):
    def __init__(self, store_id):
        self.message = f'No such store_id {store_id}'
