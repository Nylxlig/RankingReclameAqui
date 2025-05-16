from flask import Blueprint

bp_db = Blueprint("bp_db",__name__)


@bp_db.route('/')
def index():
    
    return "Hello"