import csv


def get_users():
    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [dict(i) for i in reader]
    return users


def get_stores():
    with open('stores.csv', 'r') as s:
        reader = csv.DictReader(s)
        stores = [dict(i) for i in reader]
    return stores


def get_goods():
    with open('goods.csv', 'r') as g:
        reader = csv.DictReader(g)
        goods = [dict(i) for i in reader]
    return goods