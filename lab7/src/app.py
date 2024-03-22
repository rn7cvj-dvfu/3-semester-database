from flask import Flask 
from src.config import DATABASE_URL 



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  DATABASE_URL