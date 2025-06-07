# Returning JSON Responses:
# When building APIs, you&#39;ll often want to return data in JSON format. Flask makes this
# easy: if you return a Python dictionary or list from a view function, Flask will
# automatically convert it to a JSON response and set the Content-Type header to
# application/json.
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return f"welcome"
@app.route('/api/user_data')
def user_data():
    user = {
        "id" : 1,
        "name" : "yaksh",
        "email" : "yaksh@del.hdit.com",
        "isActive" : True
    }
    return user
@app.route('/api/items')
def items_list():
    list = ["apple", "banana", "cherry"]
    return jsonify(items=list, count=len(list)), 200 # returns json and http 200 ok 
@app.route('/add/<a>/<b>')
def add_numbers_api(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        result_sum = num_a + num_b
        reponse = {
            'input_a': num_a,
            'input_b': num_b,
            'result' : result_sum,
            'operation' : 'addition'
        }
        return reponse 
    except ValueError:
        error_reponse = {
            'error': 'invalid input. please provide integers for a and b'
        }

if __name__ == "__main__":
    app.run(debug=True)