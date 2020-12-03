from app import app
from flask import render_template,request,redirect
import utils
from filters import to_uppercase
from models import User
from app import login
from flask_login import login_user


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def product_list():
    products = utils.read_products()
    return render_template("base/section.html",products=products)




@app.route('/login',methods=['get','post'])
def admin_login():
    
    if request.method == 'POST':
        username =request.form.get('username')
        password =request.form.get('password')

        user= User.query.filter(User.username == username,
                               User.password == password,
                               User.type == 0).first()
        
        if user:
            login_user(user=user)
        #else:
         #   err_msg = "LOGIN FAILED"

    return redirect('/admin')


@login.user_loader
def get_user(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    from admin_module import LogoutView,CategoryModelView
    app.run(debug=True)
