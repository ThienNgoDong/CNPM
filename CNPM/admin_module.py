from app import admin, db, app
from models import StudentProfile, Product, User, Category, ListClass
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect, request, render_template


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')

    def is_accessible(self):
        return current_user.is_authenticated

# Tiếp nhận học sinh


class StudentProfileViewModel(ModelView):
    column_display_pk = True
    can_export = True
    can_edit = True

    def is_accessible(self):
        return current_user.is_authenticated

# Lập danh sách lớp


class listclass(BaseView):
    @expose('/')
    def index(self):
        all_data = ListClass.query.all()
        return self.render('admin/dslop.html', listcourse=all_data)

    def is_accessible(self):
        return current_user.is_authenticated

# Lập danh sách học sinh


# Bảng điểm


class transcript(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        return current_user.is_authenticated

# Báo cáo


class chart(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/chart.html')

    def is_accessible(self):
        return current_user.is_authenticated


# Quy định
class Rule(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


class CategoryModelView(ModelView):
    column_display_pk = True
    can_export = True


class UserView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(StudentProfileViewModel( StudentProfile, db.session, name="Tiếp nhận học sinh"))
admin.add_view(listclass( name="Lập danh sách lớp"))
admin.add_view(transcript(name='Nhận bảng điểm môn'))
admin.add_view(chart(name="Báo cáo tổng kết"))
admin.add_view(Rule(name="Thay đổi quy định"))
admin.add_view(UserView(User, db.session))
admin.add_view(LogoutView(name="Đăng xuất"))
