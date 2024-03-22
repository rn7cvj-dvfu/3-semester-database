from src.db.db import db

from src.db.models.employee import Employee
from src.db.models.project import Project

class Task(db.Model):
    tablename = 'tasks'
    
    TaskID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey(Project.ProjectID), nullable=False)
    EmployeeID = db.Column(db.Integer, db.ForeignKey(Employee.EmployeeID), nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Status = db.Column(db.String, nullable=False)
    Priority = db.Column(db.Integer, nullable=False)
    TimeSpent = db.Column(db.Float, nullable=True) # Nullable as time can be entered later
    Deadline = db.Column(db.DateTime, nullable=False)