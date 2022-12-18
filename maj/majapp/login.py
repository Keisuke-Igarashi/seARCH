from flask import (
    Blueprint, render_template, request
)

bp = Blueprint('login', __name__)


@bp.route('/login', methods=('GET', 'POST'))
def login():

    return render_template('login.html')
