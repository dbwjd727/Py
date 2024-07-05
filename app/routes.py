from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.services import UserService, PocketmonService

main = Blueprint('main', __name__)

@main.route('/swagger/')
def swagger_ui():
    from flask import send_from_directory
    return send_from_directory('static', 'swagger-ui.html')

@main.route('/')
def index():
    return render_template('home.html')

#회원 목록 페이지
@main.route('/user/list')
def list_user():
    users = UserService.get_all_users()
    return render_template('user/list.html', users=users )

#회원가입 페이지
@main.route('/user/insert', methods=['GET','POST'])
def insert_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            return "이름 또는 이메일을 모두 입력해주세요."

        # UserService를 사용하여 사용자 생성
        user = UserService.create_user(name, email)

        # 사용자 생성 후, 다른 페이지로 리다이렉트할 수 있습니다.
        return redirect(url_for('main.index'))

    # GET 요청일 때는 폼을 렌더링합니다.
    return render_template('user/insert.html')

#수정
@main.route('/user/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()  # 클라이언트에서 전송한 JSON 데이터 받기
    new_name = data.get('name')
    new_email = data.get('email')

    if UserService.update_user(user_id, new_name, new_email):
        return jsonify({'message': '수정 완료'}), 200
    else:
        return jsonify({'error': '사용자를 찾을 수 없습니다.'}), 404
    

#삭제
@main.route('/user/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if UserService.delete_user(user_id):
        return jsonify({'message': '삭제 완료'}), 200
    else:
        return jsonify({'error', '실패'}), 404


#로그인 페이지
@main.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')

        if not email or not name:
            return "둘 다 작성해라"
        
        #사용자 인증
        user = UserService.login_user(email, name)
        if user:
            #성공시 홈으로
            return redirect(url_for('main.index'))
        else:
            return "틀림 ㅋㅋ"
        
    return render_template('user/login.html')

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
    
