from .models import User

class UserService:
    @staticmethod
    def get_all_usernames():
        users = User.query.with_entities(User.name).all()
        return [user.name for user in users]
    
    @staticmethod
    def get_all_userId():
        users = User.query.with_entities(User.id).all()
        return [user.id for user in users]
