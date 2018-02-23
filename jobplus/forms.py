from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length, Email
from jobplus.models import db, User


class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(), Email()])
    #nickname = StringField(u'昵称', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(6,24)])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError(u'密码错误')

class UserRegisterForm(FlaskForm):
    nickname = StringField(u'昵称', validators=[DataRequired(), Length(1,30)])
    email = StringField(u'邮箱', validators=[DataRequired(), Email()])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(6,24)])
    password2 = PasswordField(u'重复密码', validators=[DataRequired(), EqualTo('password', message=u'两次密码必须一致')])
    submit = SubmitField(u'用户注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError(u'该昵称已注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该邮箱已注册')

    def create_user(self):
        user = User(nickname=self.nickname.data, email=self.email.data, password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user

class CompanyRegisterForm(FlaskForm):
    company_name = StringField(u'公司名', validators=[DataRequired(), Length(1,30)])
    email = StringField(u'企业邮箱', validators=[DataRequired(), Email()])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(6,24)])
    password2 = PasswordField(u'重复密码', validators=[DataRequired(), EqualTo('password', message=u'两次密码>必须一致')])
    submit = SubmitField(u'企业注册')

    def validate_company_name(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError(u'该公司名已注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该企业邮箱已注册')

    def create_user(self):
        user = User(nickname=self.company_name.data, email=self.email.data, password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user
