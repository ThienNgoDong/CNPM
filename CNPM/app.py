from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
app = Flask(__name__)


 # Cấu hình Mysql
app.secret_key ="Sdasdasdaddsadasda"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:thangdeptrai123@@localhost/sale02db?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app=app)

admin = Admin(app=app,name="HỆ THỐNG QUẢN LÍ HỌC SINH",template_mode='bootstrap3')
login=LoginManager(app=app)