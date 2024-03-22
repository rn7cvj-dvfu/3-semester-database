from src.db.db import db

from src.db.models.project import Project

class Client(db.Model):
    tablename = 'clients'
    
    ClientID = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String, nullable=False)
    ContactName = db.Column(db.String, nullable=False)
    ContactEmail = db.Column(db.String, nullable=False)
    ContactPhone = db.Column(db.String, nullable=False)
    ProjectID = db.Column(db.Integer, db.ForeignKey(Project.ProjectID), nullable=False)
    TotalSpend = db.Column(db.Float, nullable=True) # Nullable as it can be calculated later
    Feedback = db.Column(db.Text, nullable=True) # Nullable as feedback may not be provided immediately