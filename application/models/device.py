from application import db
from datetime import datetime

# Modelo de Device
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(50), unique = False)
    device_lalitude = db.Column(db.Integer, unique = False)
    device_longitude = db.Column(db.Integer, unique = False)
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, device_name, device_lalitude, device_longitude):
      self.device_name = device_name
      self.device_lalitude = device_lalitude
      self.device_longitude = device_longitude