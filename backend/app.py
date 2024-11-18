# backend/app.py
from flask import Flask, request, jsonify
from models import db, DeviceData, LogEntry
from anomaly_detection import detect_anomalies
from log_monitoring import monitor_logs
from email_alerts import send_email_alert
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/api/device-data', methods=['POST'])
def add_device_data():
    try:
        data = request.get_json()
        heart_rate = data['heart_rate']
        glucose_level = data['glucose_level']
        timestamp = datetime.datetime.now()

        new_device_data = DeviceData(heart_rate=heart_rate, glucose_level=glucose_level, timestamp=timestamp)
        db.session.add(new_device_data)
        db.session.commit()

        # Anomaly detection
        anomalies = detect_anomalies(heart_rate, glucose_level)
        if anomalies:
            send_email_alert("Anomaly detected in device data", str(anomalies))

        return jsonify({"message": "Device data added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/device-data', methods=['GET'])
def get_device_data():
    try:
        data = DeviceData.query.all()
        results = [{"heart_rate": d.heart_rate, "glucose_level": d.glucose_level, "timestamp": d.timestamp} for d in data]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/logs', methods=['POST'])
def add_log_entry():
    try:
        data = request.get_json()
        log_message = data['log_message']
        timestamp = datetime.datetime.now()

        new_log_entry = LogEntry(log_message=log_message, timestamp=timestamp)
        db.session.add(new_log_entry)
        db.session.commit()

        # Log monitoring for suspicious activity
        monitor_logs(log_message)
        return jsonify({"message": "Log entry added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
