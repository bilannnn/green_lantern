import csv

with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    users = [i for i in reader]

with open('stores.csv', 'r') as s:
    reader = csv.DictReader(s)
    stores = [i for i in reader]

with open('goods.csv', 'r') as g:
    reader = csv.DictReader(g)
    goods = [i for i in reader]