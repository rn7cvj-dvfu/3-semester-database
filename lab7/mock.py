from src.db.db import db
from src.app import app

from src.db.models.project import Project
from src.db.models.employee import Employee
from src.db.models.task import Task
from src.db.models.client import Client
from datetime import datetime

projects = [
    Project(ProjectName='App Development', Deadline=datetime(2023, 12, 31), Budget=50000),
    Project(ProjectName='Website Redesign', Deadline=datetime(2023, 6, 30), Budget=15000),
]

employees = [
    Employee(Name='Alice Smith', Specialization='Backend Developer', HourlyRate=50),
    Employee(Name='Bob Johnson', Specialization='Frontend Developer', HourlyRate=50),
]

tasks = [
    Task(ProjectID=1, EmployeeID=1, Description='Setup project repository', Status='Completed', Priority=1, TimeSpent=2, Deadline=datetime(2023, 1, 15)),
    Task(ProjectID=1, EmployeeID=2, Description='Design initial UI/UX', Status='In Progress', Priority=2, TimeSpent=5, Deadline=datetime(2023, 1, 30)),
]

clients = [
    Client(CompanyName='TechCorp', ContactName='John Doe', ContactEmail='johndoe@techcorp.com', ContactPhone='1234567890', ProjectID=1),
    Client(CompanyName='DesignFirm', ContactName='Jane Roe', ContactEmail='janeroe@designfirm.com', ContactPhone='0987654321', ProjectID=2),

]


with app.app_context():
    # Add the sample data to the session
    for project in projects:
        db.session.add(project)

    for employee in employees:
        db.session.add(employee)

    for task in tasks:
        db.session.add(task)

    for client in clients:
        db.session.add(client)

# Commit the session to save the data to the database   
    db.session.commit()

print("Data successfully added to the database!")