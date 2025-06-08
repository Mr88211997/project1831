from flask import Flask, render_template, request
from datetime import datetime as dt 
import requests
BACKEND_URL = '127.0.0.1:9000'
app = Flask(__name__)

@app.route('/')
def index():
    current_date = dt.now()
    return render_template('index.html', current_date=current_date)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
    response = requests.post(f'{BACKEND_URL}/list', json={username: username, password: password})
    return str(response.json())
    
    

if __name__ == '__main__':
    app.run(debug = True)