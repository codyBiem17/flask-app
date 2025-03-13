from flask import Flask, jsonify, request
import datetime
import os

app = Flask(__name__)

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to get current server time
@app.route('/time', methods=['GET'])
def get_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"current_time": current_time})

# Endpoint to reverse a string
@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.json
    text = data.get('text', '')
    reversed_text = text[::-1]
    return jsonify({"original": text, "reversed": reversed_text})

# Endpoint to get environment variables
@app.route('/env', methods=['GET'])
def get_env():
    env_vars = {key: value for key, value in os.environ.items()}
    return jsonify(env_vars)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
