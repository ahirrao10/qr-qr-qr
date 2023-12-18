# serverflask.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/input', methods=['GET', 'POST'])
def receive_input():
    if request.method == 'POST':
        data = request.get_json()

        # Load existing data
        try:
            with open("user_data.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        # Append new data to existing data
        existing_data.append(data)

        # Save all data
        with open("user_data.json", "w") as file:
            json.dump(existing_data, file)

        return jsonify({"message": "Data received successfully"})
    elif request.method == 'GET':
        # Retrieve all data from the JSON file and send it as the response
        try:
            with open("user_data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000)
