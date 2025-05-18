from flask import Blueprint

bp_company = Blueprint("company", __name__)

@bp_company.route("/", methods = ["GET"])
def myFunc():
    return "Hello"