from flask import Flask, render_template
from jobplus.config import configs
from jobplus.models import db
from flask_migrate import Migrate
from jobplus.handlers import front, company, user, admin, job

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)


def register_blueprints(app):
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(company)
    app.register_blueprint(user)
    app.register_blueprint(job)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)

    return app

