from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import time


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///mydb.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = 'sbsbzvzhzbans'
db = SQLAlchemy(app) 
app.app_context().push()



from mainApp import routes

