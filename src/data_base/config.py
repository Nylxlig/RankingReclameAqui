import datetime
class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{datetime.date.today().strftime("%d-%m-%Y")}.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False