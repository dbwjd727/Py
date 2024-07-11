from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Flask
from app.services import UserService, PocketmonService
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

main = Blueprint('main', __name__)

@main.route('/swagger/')
def swagger_ui():
    from flask import send_from_directory
    return send_from_directory('static', 'swagger-ui.html')

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/map')
def map():
    return render_template('map.html')

#회원 목록 페이지
@main.route('/user/list')
def list_user():
    users = UserService.get_all_users()
    return render_template('user/list.html', users=users )

# 마이페이지
@main.route('/info', methods=['GET'])
def get_user_info():
    login_id = request.args.get('loginId')

    user = UserService.get_user_info(login_id)
    print(':::::::가져온 정보::::::::', user)  


    if not user:
        return jsonify({"error": "사용자를 찾을 수 없습니다."}), 404

    user_info = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "grade": user.grade,
        "created_at": user.created_at.strftime('%Y-%m-%d %H:%M:%S')  # 예시: 시간 포맷 변경
    }

    return jsonify(user_info), 200
    

#회원가입 페이지
@main.route('/user/insert', methods=['POST'])
def insert_user():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"error": "이름 또는 이메일을 모두 입력해주세요."}), 400

        # UserService를 사용하여 사용자 생성
        user = UserService.create_user(name, email)

       # 사용자 생성 후 성공 메시지 반환
        return jsonify({"success": True, "message": "User created successfully!"})

    return jsonify({"error": "Invalid request method."}), 405


#수정
@main.route('/user/update', methods=['PUT'])
def update_user():

    data = request.get_json()  # 클라이언트에서 전송한 JSON 데이터 받기
    login_id = data.get('loginId')
    new_name = data.get('name')
    new_email = data.get('email')

    # print('::::::::::::클라이언트 입력!!!!!!!:::::::::', login_id,new_name, new_email)

    if UserService.update_user(login_id, new_name, new_email):
        return jsonify({'message': '수정 완료','loginId': login_id, 'name': new_name, 'email': new_email}), 200
    else:
        return jsonify({'error': '사용자를 찾을 수 없습니다.'}), 404
    

#삭제
@main.route('/user/delete', methods=['DELETE'])
def delete_user():
    login_id = request.args.get('loginId')
    print(':::::::탈퇴할 아이디::::::::', login_id)

    if UserService.delete_user(login_id):
        return jsonify({'message': '삭제 완료'}), 200
    else:
        return jsonify({'error', '실패'}), 404


#로그인 페이지
@main.route('/login', methods=['POST'])
def login_user():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        
        if not name or not email:
            return jsonify({"error": "이름과 이메일을 모두 입력해주세요."}), 400
        
        # 사용자 인증
        user = UserService.login_user(name, email)
        if user:
            # 성공시 홈으로 리다이렉트 혹은 성공 메시지 반환
            return jsonify({"success": True, "message": "로그인 성공!"})
        else:
            return jsonify({"error": "로그인 실패. 이름 또는 이메일이 일치하지 않습니다."}), 401

    # GET 요청은 여기서 처리하지 않음
    return jsonify({"error": "POST 메서드만 지원됩니다."}), 405




#포켓몬 목록
@main.route('/pocketmon/list')
def list_pocketmon():
    pocketmons = PocketmonService.get_all_pocketmon()
    return render_template('pocketmon/list.html', pocketmon=pocketmons )

#포켓몬 등록
@main.route('/pocketmon/insert', methods=['GET','POST'])
def insert_pocketmon():
    if request.method == 'POST':
        name = request.form.get('name')
        type = request.form.get('type')

        if not name or not type:
            return "둘 다 입력하삼"
        
        pocketmon = PocketmonService.create_pocketmon(name, type)
        return redirect(url_for('main.index'))
    
    return render_template('pocketmon/insert.html')

#포켓몬 수정
@main.route('/pocketmon/update/<int:pocketmon_id>', methods=['PUT'])
def update_pocketmon(user_id):
    data = request.get_json()  # 클라이언트에서 전송한 JSON 데이터 받기
    new_name = data.get('name')
    new_type = data.get('type')

    if UserService.update_pocketmon(user_id, new_name, new_type):
        return jsonify({'message': '수정 완료'}), 200
    else:
        return jsonify({'error': '사용자를 찾을 수 없습니다.'}), 404
    