from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/sensor-data')
def sensor_data():
    data = {
        "soil_moisture": random.randint(30, 90),
        "temperature": random.randint(20, 40),
        "humidity": random.randint(40, 80)
    }

    spray_status = "ON" if data["soil_moisture"] < 50 else "OFF"

    data["spray_status"] = spray_status

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

