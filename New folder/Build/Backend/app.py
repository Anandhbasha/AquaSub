from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
import jwt
import datetime
from waitress import serve

try:
    from db import users
except Exception as e:
    print("Error connecting to MongoDB:", e)
    exit()

try:
    with open("Key.txt", "r") as f:
        SECRET_KEY = f.read().strip()
except Exception as e:
    print("Error reading Key.txt:", e)
    exit()

app = Flask(__name__)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    if users.find_one({'username': username}):
        return jsonify({'msg': 'User already exists'}), 400

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users.insert_one({'username': username, 'password': hashed_pw})

    return jsonify({'msg': 'Registered successfully'})


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = users.find_one({'username': username})
    if not user:
        return jsonify({'msg': 'Invalid user'}), 401

    if bcrypt.checkpw(password.encode('utf-8'), user['password']):
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'msg': 'Login success', 'token': token})
    else:
        return jsonify({'msg': 'Incorrect password'}), 401

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'msg': 'Token missing'}), 403

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'msg': 'Welcome to protected route', 'user': decoded['username']})
    except jwt.ExpiredSignatureError:
        return jsonify({'msg': 'Token expired'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'msg': 'Invalid token'}), 403

if __name__ == '__main__':
    print("🚀 Starting Flask App on port 5050")
    serve(app, host="127.0.0.1", port=5050)