from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from app.models import db
import logging
from app import create_app


app = Flask(__name__)
app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
