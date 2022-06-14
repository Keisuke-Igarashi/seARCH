from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

import ast

from majapp.db import get_db


bp = Blueprint('search', __name__)

@bp.route('/search', methods=('GET', 'POST'))
def search():

    result = ""
    result2 = ""
    
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
          

                # 建築家名から建築家IDを取得する
                search_word = "%" + archiname + "%"
                sql = "SELECT * FROM architect WHERE architect_name LIKE %s;"
                cursor.execute(sql,(search_word,))
                result = cursor.fetchall()
                result_dict = result[0]
                archiname_id = result_dict['architect_id']

                # 建築家IDから建築物を取得する
                search_word = archiname_id
                sql = "SELECT * FROM architecture WHERE architect_id = %s;"
                cursor.execute(sql,(search_word,))
                result2 = cursor.fetchall()

            
            print(type(result))
            print(result_dict)

            connect.close()

    return render_template('search.html', archs = result2)