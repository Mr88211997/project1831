from flask import Flask, render_template, request
from datetime import datetime as dt
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


DB_HOST = 'localhost'
#DB_PORT = '3307'
DB_USER = 'root'  # e.g., 'root'
DB_PASSWORD = 'Yaksh@8821'
DB_NAME = 'welcome'

def get_db_connection():
    conn = mysql.connector.connect(
            host=DB_HOST,
           # port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    return conn
@app.route('/')
def index():
    # current_date = dt.now()
    return "working" #render_template('index.html', current_date=current_date)



@app.route('/list')
def list():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    # users = dict(users)
    return users

if __name__ == '__main__':
    app.run(debug = True, port=9000)