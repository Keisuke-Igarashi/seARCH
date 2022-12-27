from flask import (
    Blueprint, flash, render_template, request
)

bp = Blueprint('user_register', __name__)


@bp.route('/user_register', methods=('GET', 'POST'))
def register():

    # 初期変数設定
    
    return render_template('user_register.html')
