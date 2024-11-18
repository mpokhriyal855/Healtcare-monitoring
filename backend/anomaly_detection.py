# backend/anomaly_detection.py
from sklearn.ensemble import IsolationForest
import numpy as np

# Sample model: Isolation Forest for anomaly detection
def detect_anomalies(heart_rate, glucose_level):
    model = IsolationForest(n_estimators=100, contamination=0.05)
    data = np.array([[heart_rate, glucose_level]])
    
    # Fit the model with historical data
    # (In practice, this should be done once, and the model should be saved for reuse)
    historical_data = np.array([
        [80, 100],  # Normal data
        [90, 110],  # Normal data
        [85, 105],  # Normal data
        [120, 200],  # Anomalous data
        [160, 250]   # Anomalous data
    ])
    
    model.fit(historical_data)
    prediction = model.predict(data)

    if prediction == -1:
        return f"Anomalous data detected: Heart Rate: {heart_rate}, Glucose: {glucose_level}"
    return None
