from src.db.db import db

class Employee(db.Model):
    tablename = 'employees'
    
    EmployeeID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Specialization = db.Column(db.String, nullable=False)
    HourlyRate = db.Column(db.Float, nullable=False)