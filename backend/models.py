# # backend/models.py
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class DeviceData(db.Model):
#     __tablename__ = 'device_data'

#     id = db.Column(db.Integer, primary_key=True)
#     heart_rate = db.Column(db.Float, nullable=False)
#     glucose_level = db.Column(db.Float, nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False)
    
#     def __repr__(self):
#         return f"<DeviceData {self.id} - {self.heart_rate} bpm - {self.glucose_level} mg/dL>"

# class LogEntry(db.Model):
#     __tablename__ = 'logs'

#     id = db.Column(db.Integer, primary_key=True)
#     log_message = db.Column(db.String(255), nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False)

#     def __repr__(self):
#         return f"<LogEntry {self.id} - {self.log_message}>"
