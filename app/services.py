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
    
    #로그인
    @staticmethod
    def login_user(name, email):
        user = User.query.filter_by(name=name, email=email).first()
        print(':::::::::::로그인시도한 유저::::::::::::', name, email)

        if user:
            print(':::::::::::찾은 유저::::::::::::', user.name, user.email)

        if user and user.name == name and user.email == email:
            return user
        return None
    
    # 사용자 정보 업데이트하기
    @staticmethod
    def update_user(login_id, new_name, new_email):
        user = User.query.filter_by(name=login_id).first()
        # print(':::::::::::로그인한 유저 이름::::::::::::', user)
        # 사용자가 존재하는지 확인
        if user:
            # name이 제공된 경우 업데이트
            if new_name:
                user.name = new_name
                # print(':::::::::바뀐 아이디::::::::', new_name)
            # email이 제공된 경우 업데이트
            if new_email:
                user.email = new_email
                # print(':::::::::바뀐 이메일::::::::', new_email)

            # 변경 사항을 데이터베이스에 반영
            db.session.commit()

            return True  # 업데이트 성공
        else:
            return False  # 사용자가 존재하지 않음
        
    # 사용자 정보 삭제하기
    @staticmethod
    def delete_user(login_id):
        #조회
        user = User.query.filter_by(name=login_id).first()

        print(':::::::::::로그인한 유저 이름::::::::::::', user)

        if user:
            db.session.delete(user)
            db.session.commit()

            return True
        else:
            return False

    #내정보 출력
    @staticmethod
    def get_user_info(login_id):
        #조회
        user = User.query.filter_by(name=login_id).first()

        if user:
            return user
        else:
            return None
    
###pocketmon
class PocketmonService:
    #모든 정보 출력
    @staticmethod
    def get_all_pocketmon():
        return Pocketmon.query.all()
    
    #insert
    @staticmethod
    def create_pocketmon(name, type):
        new_pocketmon = Pocketmon(name = name, type = type)

        db.session.add(new_pocketmon)
        db.session.commit()

        return new_pocketmon
    
    #포켓몬 수정
    @staticmethod
    def update_pocketmon(id, name, type):
        pocketmon = User.query.get(id)

        # pocketmon 존재하는지 확인
        if pocketmon:
            if name:
                pocketmon.name = name
            if type:
                pocketmon.type = type

            # 변경 사항을 데이터베이스에 반영
            db.session.commit()

            return True  # 업데이트 성공
        else:
            return False  # 사용자가 존재하지 않음