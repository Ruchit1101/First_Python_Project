import enum
from . import db
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Numeric 
# import enum

# db = SQLAlchemy()

class GenderEnum(enum.Enum):
       male = 'Male'
       femal = 'Female'
       other = 'Other'

class Students(db.Model):
       __tablename__='Students'
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(100), nullable=False)
       gender = db.Column(db.Enum(GenderEnum), nullable=False)
       maths_marks = db.Column(Numeric(precision=3, scale=2))
       science_marks = db.Column(Numeric(precision=3, scale=2))
       social_marks = db.Column(Numeric(precision=3, scale=2))


       def __repr__(self):
            return f'<Students {self.name}>'