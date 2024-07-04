from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.services import UserService

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "hello world!!!!!!!"

@main.route('/insert', methods=['GET', 'POST'])
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
    return render_template('insert.html')