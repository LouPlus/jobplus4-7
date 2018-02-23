#基本配置
class BaseConfig(object):
    SECRET_KEY = 'project jobplus'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'
    #跟踪修改对象，发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = True

#开发配置
class DevelopmentConfig(BaseConfig):
    DEBUG = True

#产品配置
class ProductionConfig(BaseConfig):
    pass

#测试配置
class TestingConfig(BaseConfig):
    Testing = True


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
