from mainApp import db
from datetime import datetime

'''Db model for Afternoon classes youth'''
class After_noon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_no = db.Column(db.Integer, nullable=False)
    acadamy = db.Column(db.String(100), nullable=False)
    church = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, sex, age, phone_no, acadamy, church):
        self.name = name
        
        self.sex = sex
        self.age = age
        self.phone_no = phone_no
        self.acadamy = acadamy
        self.church = church
        if not name or not age or not sex or not phone_no or not acadamy or not church:
        	raise ValueError("Fill the spaces correclt")
    def __repr__(self):
        return f'{self.id}- {self.name}-{self.sex}- {self.sex}- {self.age}- {self.phone_no}- {self.acadamy}- {self.church}'

'''Db model for yeen agers uder 15'''
class Morning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_no = db.Column(db.Integer, nullable=False)
    acadamy = db.Column(db.String(100), nullable=False)
    church = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, sex, age, phone_no, acadamy, church):
        self.name = name
        self.sex = sex
        self.age = age
        self.phone_no = phone_no
        self.acadamy = acadamy
        self.church = church
        if not name or not age or not sex or not phone_no or not acadamy or not church:
        	raise ValueError("Fill the spaces correclt")

    def __repr__(self):
        return f'{self.id}| {self.name}| {self.sex}| {self.sex}| {self.age}| {self.phone_no}| {self.acadamy}| {self.church}'

#weeks = [1,2 ,3 ,4, 5]
#weekdays = ['Monday', 'Tuesday', "Wensday", "Thursday", "Friday"]

class attend_after(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    w1_d1 = db.Column(db.String(30))
    w1_d2 = db.Column(db.String(30))
      
    w1_d3 = db.Column(db.String(30))
    w1_d4 = db.Column(db.String(30))
    w1_d5 = db.Column(db.String(30))
    
   
    def __init__(self, name, w1_d1, w1_d2, w1_d3, w1_d4, w1_d5):
        # self.id = id
        self.name = name
        self.w1_d1 = w1_d1
        self.w1_d2 = w1_d2
        self.w1_d3 = w1_d3
        self.w1_d4 = w1_d4 
        self.w1_d5 = w1_d5
        
        
    def __repr__(self):
        return f'{self.id}. {self.name}, {self.w1_d1} ,{self.w1_d2},  {self.w1_d3},  {self.w1_d4},  {self.w1_d5}'


