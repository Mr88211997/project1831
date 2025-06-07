# config.py
import os

class Config:
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Yaksh@8821'
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'flask'
  #  MYSQL_CURSORCLASS = 'DictCursor'  # Optional, but helps with results in dictionary form

# app.py or main.py
from flask import Flask
from flask_mysql import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

# Example: Use the connection
@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM some_table;")
    result = cursor.fetchall()
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
