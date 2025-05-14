from flask import Blueprint

bp_db = Blueprint(__name__,"bp_db")


@bp_db.route('/')
def index():
    
    return "Hello"