from .models import db, User, Pocketmon

###user
class UserService:
    #모든 정보 출력
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    #insert
    @staticmethod
    def create_user(name, email):
        new_user = User(name=name, email=email)

        db.session.add(new_user)
        db.session.commit()

        return new_user
    
    #name, email check
    @staticmethod
    def login_user(name, email):
        user = User.query.filter_by(email=email).first()
        if user and user.check_name(name):
            return user
        return None
    
    # 사용자 정보 업데이트하기
    @staticmethod
    def update_user(id, name=None, email=None):
        # 사용자 조회
        user = User.query.get(id)

        # 사용자가 존재하는지 확인
        if user:
            # name이 제공된 경우 업데이트
            if name:
                user.name = name
            # email이 제공된 경우 업데이트
            if email:
                user.email = email

            # 변경 사항을 데이터베이스에 반영
            db.session.commit()

            return True  # 업데이트 성공
        else:
            return False  # 사용자가 존재하지 않음
        
    # 사용자 정보 삭제하기
    @staticmethod
    def delete_user(id):
        #조회
        user = User.query.get(id)

        if user:
            db.session.delete(user)
            db.session.commit()

            return True
        else:
            return False


        
    
###pocketmon
class PocketmonService:
    #insert
    @staticmethod
    def create_pocketmon(name, type):
        new_pocketmon = Pocketmon(name = name, type = type)

        db.session.add(new_pocketmon)
        db.session.commit()

        return new_pocketmon