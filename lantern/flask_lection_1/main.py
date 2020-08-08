
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello qq"




@app.route("/name",methods =["GET", "POST"])
def name():
    resp = "Name"
    response = make_response(resp_data)
    response.headers = {"Costom_header": "Custom_header_value"}
    return  response

@app.errorhandler(404)
def page_not_found(error):
    return render_template('<><>'),404

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method =='POST':
        return "POST"
    else:
        return "show_the_login_form()"

@app.route('/number/<int:num_value>')
def get_number(num_value):
    print(type(num_value))
    return f"{num_value}"


if __name__ == "__main__":
    app.run(debug=True)
