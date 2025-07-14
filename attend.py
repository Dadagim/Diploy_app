from flask import Flask, render_template, request, redirect,Blueprint, session
from flask_session import Session
from mainApp.model import After_noon, Morning, attend_after, db
from datetime import datetime


attendace = Blueprint('attendance', __name__)


@attendace.route('/after')
def attend():
    
    name = 'Dagim Dawit'
    u1 = attend_after(name, 'Present', 'Late', 'Absent', "Present", "Present")       
    db.session.add(u1)
    db.session.commit()
    after = attend_after.query.all()
    return str(after)