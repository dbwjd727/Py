# config.py
class Config:
    SECRET_KEY = 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:maria@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

 