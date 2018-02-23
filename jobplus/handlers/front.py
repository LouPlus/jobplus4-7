from flask import Blueprint, render_template, flash, url_for, redirect
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm
from jobplus.models import db, User
from flask_login import login_user, login_required, logout_user

front = Blueprint('front', __name__)

#主页
@front.route('/')
def index():
    return render_template('index.html')

#登录
@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        flash(u'登录成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('login.html', form=form)

#注销
@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'注销成功', 'success')
    return redirect(url_for('front.index'))

#企业注册
@front.route('/companyRegister', methods=['GET', 'POST'])
def company_register():
    form = CompanyRegisterForm()
    if form.validate_on_submit():
        user = form.create_user()
        user.role = User.ROLE_COMPANY
        db.session.add(user)
        db.session.commit()
        flash(u'企业注册成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('company_register.html', form=form)

#求职者注册
@front.route('/userRegister', methods=['GET', 'POST'])
def user_register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash(u"注册成功", 'success')
        return redirect(url_for('front.index'))
    return render_template('user_register.html', form=form)


