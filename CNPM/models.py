from sqlalchemy import Column, Integer, String, Float, ForeignKey, or_, and_, Date, Boolean
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime
from flask_login import UserMixin


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    product = relationship('Product', backref="category", lazy=True)


def __str__(self):
        return self.name


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, default=0)
    created_date = Column(Date, default=datetime.now())
    active = Column(Boolean, default=True)
    image = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    type = Column(Integer)  # 0-admin, 1-giaovien, 2-hocsinh

    def __str__(self):
        return self.name



class ListClass(db.Model):
    __tablename__ = "listclass"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classroom = Column(String(50), nullable=False)
    siso =Column(Integer)

    def __init__(self,classroom):
        self.classroom = classroom

class StudentProfile(db.Model):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    sex = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    address = Column(String(250))
    email = Column(String(250))
    classroomID = Column(Integer,ForeignKey(ListClass.id), nullable=False)

class Teacher(db.Model):
    __tablename__ = "teacher"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name =Column(String(50),nullable =False)
    avatar = Column(String(100))
    sex =Column(String(50),nullable =False)
    date = Column(Date,nullable=False)
    status = Column(String(50))
    address = Column(String(250))
    phone =Column(String(12))

class Subjects(db.Model):
    __tablename__ = "subject"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name =Column(String(50),nullable =False)
    
class Score(db.Model):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentID = Column(Integer,ForeignKey(StudentProfile.id), nullable=False)
    subjectID = Column(Integer,ForeignKey(Subjects.id), nullable=False)
    Score15 = Column(Float, default=0)
    Score1T = Column(Float, default=0)
    semester = Column(String(10),nullable=False)
    createDate = Column(Date, default=datetime.now())

if __name__ == "__main__":
    db.create_all()
