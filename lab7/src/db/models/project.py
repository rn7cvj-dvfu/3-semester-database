from src.db.db import db

class Project(db.Model):
    tablename = 'projects'
    
    ProjectID = db.Column(db.Integer, primary_key=True)
    ProjectName = db.Column(db.String, nullable=False)
    Deadline = db.Column(db.DateTime, nullable=False)
    Budget = db.Column(db.Float, nullable=False)