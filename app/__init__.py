from flask import Flask
from .db import init_app, db
from .routes import main
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_app(app)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()  # 데이터베이스 테이블을 생성합니다.

    return app
