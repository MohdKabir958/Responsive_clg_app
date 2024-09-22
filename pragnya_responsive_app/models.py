from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # profile_pic = db.Column(db.LargeBinary)  # Storing image as BLOB
    student_grade = db.Column(db.Float, nullable=True)  # Float for grades
    profile_pic = db.Column(db.String(500), nullable=True)  # Column to store image path



