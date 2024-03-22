from src.app import app
from src.db.db import db

from src.db.models import  employee , project , task , client


with app.app_context():
    db.create_all()