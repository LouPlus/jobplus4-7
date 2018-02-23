from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#用户表
class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10 
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    #头像 -> 静态文件实现
    #昵称
    nickname = db.Column(db.String(32), nullable=False, unique=True)
    #邮箱
    email = db.Column(db.String(64), nullable=False, unique=True)
    #密码
    _password = db.Column('password', db.String(256), nullable=False)
    #职位
    job = db.Column(db.String(64))
    #角色
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    #对应公司
    detail = db.relationship('Company', uselist=False)

    is_disable = db.Column(db.Boolean, default=False)

    #密码属性
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    #角色属性
    @property
    def is_user(self):
        return self.role == self.ROLE_USER

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    def __repr__(self):
        return '<User {}>'.format(self.email)

#职位表
class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    #职位名称
    job_title = db.Column(db.String(40), nullable=False)
    #薪水下限
    lowest_salary = db.Column(db.SmallInteger, nullable=False)
    #薪水上限
    highest_salary = db.Column(db.SmallInteger, nullable=False)
    #工作经验
    work_experience = db.Column(db.String(40), nullable=False) 
    #工作地址之城市
    work_location_city = db.Column(db.String(40), nullable=False)
    #工作地址之区域
    work_location_district = db.Column(db.String(40), nullable=False)
    #工作地址之具体位置
    work_location_address = db.Column(db.String(120), nullable=False)
    #职位描述
    job_description = db.Column(db.Text)
    #职位要求
    job_requirements = db.Column(db.Text)
    #发布时间
    release_time = db.Column(db.DateTime, default=datetime.utcnow)
    #外键->company
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

    def __repr__(self):
        return '<Job {}>'.format(self.job_title)

#企业表
class Company(Base):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    #企业logo使用static文件实现，直接链接图片
    #企业名称
    company_name = db.Column(db.String(80), nullable=False, unique=True)
    #企业网站
    website = db.Column(db.String(80))
    #公司地址
    address = db.Column(db.String(120))
    #一句话描述
    description = db.Column(db.String(120))
    #公司详细介绍
    introduction = db.Column(db.Text)
    #企业对应的职位
    jobs = db.relationship('Job', backref='company', lazy='dynamic')
    #企业对应的企业用户
    user = db.relationship('User', uselist=False, backref=db.backref('company', uselist=False))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))

    def __repr__(self):
        return '<Comapny {}>'.format(self.company_name)
