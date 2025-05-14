from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.data_base.config import Config


db = SQLAlchemy()

def newApp():
    app = Flask(__name__)
    app.config.from_object(Config)


    from src.data_base.routes import bp_db
    app.register_blueprint(bp_db)
    db.init_app(app)


    with app.app_context():
        db.create_all()



    return app