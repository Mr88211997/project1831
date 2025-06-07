# Advanced Flask: Templates, Data Handling, and Forms
# In this section, we&#39;ll move beyond returning simple strings from our Flask routes. We&#39;ll
# learn how to serve full HTML pages, make those pages dynamic by passing data from
# our Python code, and process data submitted by users through web forms.
# 1. Serving HTML with Flask: Templates
# So far, our Flask routes have returned simple strings. To build actual web pages, we
# need to return HTML. While you could write HTML as a giant string in Python (like we
# did for the simple login page), it quickly becomes unmanageable for anything complex.
# This is where templates come in. A template is essentially an HTML file that can
# contain placeholders for dynamic data. Flask uses a powerful templating engine called
# Jinja2 (which comes installed with Flask) to render these templates.
# Directory Structure:
# By default, Flask looks for HTML template files in a folder named templates located in the
# same directory as your Flask application script (app.py).
# your_flask_project/
# ├── app.py # Your main Flask application file

# └── templates/ # Folder for HTML templates
# └── index.html # An example HTML template
# └── about.html
# └── ...
# The render_template() Function:
# To serve an HTML file from the templates folder, you import and use the render_template()
# function from Flask.
from flask import Flask, render_template # Import render_template
app = Flask(__name__)
@app.route('/')
def home():
# This will look for &#39;index.html&#39; in the &#39;templates&#39; folder
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)










