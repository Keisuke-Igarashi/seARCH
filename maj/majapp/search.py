from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from majapp.db import get_db


bp = Blueprint('search', __name__)

@bp.route('/search', methods=('GET', 'POST'))
def search():

    result = ""
    if request.method == 'POST':
        archiname = request.form['architect_name']
        error = None

        if not archiname:
            error = 'archiname is required.'

        if error is not None:
            flash(error)

        else:
          
            connect = get_db()
            with connect.cursor() as cursor:
          
                # sql = "SELECT * FROM architect WERER architect_name like %s"
                cursor.execute("SELECT * FROM architect WERER architect_name like %s",("%"+ archiname + "%",))
                result = cursor.fetchall()
            
            connect.close()

    return render_template('search.html', archs = result)