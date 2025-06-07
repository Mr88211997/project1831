from flask import Flask, render_template,request, redirect, url_for
import _mysql_connector
from _mysql_connector import Error
app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to home"
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/submit', methods = ['GET'])
def submit():
    err = "email id and password is not valid! "
    email = request.args.get('email')
    pwd = request.args.get('password')
    # msg = f"you have enter the username : {username} \n password : {password}"
    # return msg
    if email == 'demo@hdit.com':
        if pwd == '12345':
            return render_template('deshboard.html') #if you want to use jinja template  redirect(url_for('deskboard'))
        else:
            return render_template('login.hmtl', err=err ) # if you want to use jinja template redirect(url_for('login'))
    else:
        return render_template('login.html', err=err ) 

@app.route('/deshboard')
def deshboard():
    return render_template('deshboard.html')


if __name__ == "__main__":
    app.run(debug=True)