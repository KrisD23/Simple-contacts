#importing important 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 

# init the flask
app = Flask(__name__)
CORS(app) # handling the cors

# storing sql 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db= SQLAlchemy(app)