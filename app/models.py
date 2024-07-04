from .db import db

class User(db.Model):
    __tablename__ = 'users' #내가만든 테이블
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
