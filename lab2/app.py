from flask import Flask, render_template
from datetime import datetime # To get the current day

app = Flask(__name__)

@app.route('/')
def home():
    current_day = datetime.today().strftime("%A") # Gets the full weekday name (e.g., "Monday")
    user_name = "DevOps Learner"
    items = ["Learn Flask", "Build an API", "Deploy an App"]

    # Pass variables to the template
    return render_template('index.html', 
                           day=current_day, 
                           name=user_name,
                           tasks=items)

if __name__ == '__main__':
    app.run(debug=True)