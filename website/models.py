from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Peg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    status = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_user_id = db.Column(db.Integer)
    project_info = db.Column(db.String(100))
    type = db.Column(db.String(100))


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    status = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_user_id = db.Column(db.Integer)
    request_user_name = db.Column(db.String(100))
    project_name = db.Column(db.String(100))
    Technical_skills = db.Column(db.Integer)
    Communication_skills = db.Column(db.Integer)
    Team_work_skills = db.Column(db.Integer)
    Problem_solving_skills = db.Column(db.Integer)
    Time_management = db.Column(db.Integer)




class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    peg = db.relationship('Peg')
    feedback = db.relationship('Feedback')
    role = db.Column(db.String(100))
    career_level = db.Column(db.String(100))
    personal_number = db.Column(db.Integer)
    fiscal_year = db.Column(db.Integer)
    su = db.Column(db.String)
