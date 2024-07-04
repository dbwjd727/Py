from flask import Flask
from .db import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from .routes import bp
    app.register_blueprint(bp)
    
    return app
