from datetime import datetime
from flaskapp import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location = db.Column(db.String(), nullable=False)
    condition = db.Column(db.String(), nullable=False)
    wave_height = db.Column(db.String(), nullable=False)
    tide = db.Column(db.String(), nullable=False)
    wind = db.Column(db.String(), nullable=False)
    swells = db.Column(db.String(), nullable=True)
    weather = db.Column(db.String(), nullable=False)
    h20_temp = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Report('{self.location}', '{self.condition}', '{self.date}')"
