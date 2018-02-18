from flask import Blueprint,render_template

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/')
def company_index():
    return render_template('index.html')
