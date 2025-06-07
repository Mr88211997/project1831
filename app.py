
#dynamic route
from flask import Flask 
app = Flask(__name__)

app.route('/')
def home():
    return "welcome to home page "

@app.route('/about')
def about():
    return "this is the about us page"

@app.route('/contact')
def contact():
    return "contact as at the workforinfinitely1831@gmail.com"
@app.route('/user/<username>')
def profile(username):
    return f"hello, {username} this is the profile page"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"displaying post number: {post_id} (type: {type(post_id)})"

@app.route('/api/<name>')
def data_check(name):
    length = len(name)
    if length<=5:
        return f"the name '{name}' is too short (lenght:{length})"
    else:
        return f"the name '{name}' is okay (lenght:{length})"
    
if __name__ == '__main__':
    app.run(debug=True)