from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with

from module1 import module1

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', required=True, action='append', type=int)
parser.add_argument('filter', required=True)

parser_1 = parser.copy()
parser_1.replace_argument('filter')


class Cars(Resource):
    def get(self):
        args = parser.parse_args()
        return args

    def post(self):
        return "Hello from post"

    def put(self):
        return "Hello from put"


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.phones = [11, 22]
        self.address = {
            "city": "Lviv",
            "street": "Shevchenka"
        }


class Upper(fields.Raw):
    def format(self, value):
        return value.upper()


address_structure = {
    "city": fields.String,
    "street": fields.String
}
person_structure = {
    # "name": fields.String,
    "name": Upper,
    "age": fields.Integer,
    "phones": fields.List(fields.Integer),
    "address": fields.Nested(address_structure)
}


class PeopleResource(Resource):
    @marshal_with(person_structure)
    def get(self):
        return People("Jack", 12)


api.add_resource(Cars, "/cars", "/cars/<value>")
api.add_resource(PeopleResource, "/people")
app.register_blueprint(module1)

if __name__ == "__main__":
    app.run(debug=True)
