from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
client = MongoClient('mongodb://admin:pass@mongodb-svc:27017/')
db = client['my-database']
collection = db['profile']

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/profile')
def my_profile():
    profile_data = {
        "name": "John Doe - Connected form Backend",
        "email": "johndoe@example.com",
        "age": 30
    }
    return profile_data
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
