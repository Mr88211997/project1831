from flask import Flask, request 
app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to my page"

@app.route('/search')
def search():
    query_term = request.args.get('q') #use .get() to avoid errors if param is missing 
    category = request.args.get('category','all') # provide a default value 
    if query_term:
        return f" searching for '{query_term}' in category '{category}' "
    else:
        return "please provide a search term using ?q=your_query"

@app.route('/api/info')
def api_info():
    name = request.args.get('name') # for get request use request.args 
    age = request.args.get('age')
    #build a dictionary for the response 
    response_data = {}
    if name:
        response_data['name'] = name
    if age:
        response_data['age'] = age
    if not response_data:
        return f"please provide 'name' and/ or  'age' as query parameters (e.g. /api/info?name=yaksh&age=30)"
    return response_data
if __name__ == "__main__":
    app.run(debug=True)
