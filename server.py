# server.py
from flask import Flask, jsonify
import json

app = Flask(__name__)
latest_data_file = "latest_data.json"

# Endpoint to return the latest temperature data
@app.route('/sensor-data', methods=['GET'])
def get_latest_data():
    try:
        # Read the latest data from the JSON file
        with open(latest_data_file, 'r') as f:
            latest_data = json.load(f)
        return jsonify(latest_data), 200
    except FileNotFoundError:
        return jsonify({"message": "No data available"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

