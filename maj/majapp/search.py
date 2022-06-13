from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# from python.db import get_db


bp = Blueprint('search', __name__)

@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        archiname = request.form['architect_name']
        error = None

        if not archiname:
            error = 'archiname is required.'

        # if error is not None:
        flash(error)

        # else:
            # db = get_db()
            # db.execute(
            #     'INSERT INTO post (title, body, author_id)'
            #     'VALUES (?, ?, ?)',
            #     (title, body , g.user['id'])
            # )
            # db.commit()
            # return redirect(url_for('/hello'))

    from . import db
    result = get_db()

                
    return render_template('search.html')
