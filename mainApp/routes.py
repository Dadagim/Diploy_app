from mainApp import app, db
from flask import render_template, request, Blueprint
from mainApp.model import After_noon, Morning, attend_after
from attend import attendace


app.register_blueprint(attendace, url_prefix='/attend')

'''Home page remdering the main web page'''
a = After_noon.query.all()
for i in a:
    print(i)
@app.route('/')
def index():
    return render_template("index.html")
    
    
@app.route("/register", methods=["POST", 'GET'])
def register():
    if request.method =="GET":
        return 'please register by providing information needed'
    name = request.form.get("name")
    sex = request.form.get("sex")
    age = request.form.get("age")
    phone_no = request.form.get("phone")
    acadamy = request.form.get("learning-status")
    church = request.form.get("church")
    
    
    if not name or not sex or not age or not phone_no or not acadamy or not church:
        flash("Somthing is Missing")
        return 'Somthing is missing'
    if int(age) < 13:
        return 'You are too Young'
    else:
        if int(age) >15:
            after = After_noon(name, sex, age, phone_no, acadamy, church)
            db.session.add(after)
            db.session.commit()
            return f'you are Seccsusfully Registered {name} in Afternoon section'
            
        else:
            morning = Morning(name.title() , sex, age, phone_no, acadamy, church)
            db.session.add(morning)
            db.session.commit()
            
            return f'you are Seccsusfully Registered {name} in morning secsion'
            
