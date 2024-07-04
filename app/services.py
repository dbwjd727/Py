from .models import db, User

class UserService:
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def create_user(name, email):
        new_user = User(name=name, email=email)

        db.session.add(new_user)
        db.session.commit()

        return new_user
    
    