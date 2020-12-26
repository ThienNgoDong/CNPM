from app import app, db, admin
from flask import render_template, request, redirect, flash, url_for
import utils
from filters import to_uppercase
from models import User
from app import login
from flask_login import login_user
from models import ListClass, StudentProfile
from flask_sqlalchemy import SQLAlchemy
from flask_admin import BaseView, expose


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def product_list():
    products = utils.read_products()
    return render_template("base/section.html", products=products)


@app.route('/login', methods=['get', 'post'])
def admin_login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter(User.username == username,
                                 User.password == password,
                                 User.type == 0).first()

        if user:
            login_user(user=user)
        # else:
         #   err_msg = "LOGIN FAILED"

    return redirect('/admin')


@app.route('/insertcourse', methods=['get', 'post'])
def insertcourse():
    if request.method == 'POST':
        classroom = request.form['name']

        my_data = ListClass(classroom)
        db.session.add(my_data)
        db.session.commit()
        flash("Thanh cong")
        return redirect(url_for('transcript.index'))


@app.route('/admin/listclass/liststudent/<id>', methods=['GET', 'POST'])
def liststudent(id):
    my_data = StudentProfile.query.filter(StudentProfile.classroomID == id)
    class_data = ListClass.query.get(id)
    return render_template('admin/dsHS.html', listStudent=my_data , classinfo=class_data)


@login.user_loader
def get_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    from admin_module import LogoutView, CategoryModelView
    app.run(debug=True)
