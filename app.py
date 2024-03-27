from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__, static_url_path='', static_folder='')

connection_string = "mongodb+srv://user1:user1@cluster0.iqiren5.mongodb.net/"
client = MongoClient(connection_string)
db = client['user_db']
collection = db['users']

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data['name']
    email = data['email']
    collection.insert_one({'name': name, 'email': email})
    return jsonify({'message': 'Data inserted successfully'})

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)



    # NsHfMbEUr5NQ0Inx
    # 182.177.29.102
