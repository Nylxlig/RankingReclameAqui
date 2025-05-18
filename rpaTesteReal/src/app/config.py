import datetime
date_today = datetime.date.today().strftime("%d-%m-%Y")

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{date_today}.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False