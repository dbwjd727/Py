from flask import Flask
from .db import init_app, db
from .routes import main
from config import Config
from flask_cors import CORS
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_app(app)

    app.register_blueprint(main)

    # CORS 정책 설정
    CORS(app)

     # 로그 설정
    if not app.debug:
        app.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('app.log')
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.addHandler(file_handler)

    with app.app_context():
        db.create_all()  # 데이터베이스 테이블을 생성합니다.

    return app
