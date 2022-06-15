from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

import ast
import json

from majapp.db import get_db

bp = Blueprint('favorite', __name__)

@bp.route('/favorite', methods=('GET', 'POST'))
def favorite():

    result = ""
    result2 = ""
    
    if request.method == 'POST':
        
        param = json.loads(request.data.decode('utf-8'))
        print(param);
        architecture_id = param['architecture_id']
        error = None

        if not architecture_id:
            error = 'architecture_id is required.'

        if error is not None:
            flash(error)

        else:
          
            # result2 = architecture_id
            connect = get_db()

            with connect.cursor() as cursor:
          
                # お気に入りデータを登録する
                sql_1 = "INSERT INTO favorite (user_id, architecture_id) VALUES (%s, %s);"
                cursor.execute(sql_1,('1', architecture_id,))
                
            connect.commit()

            with connect.cursor() as cursor:

                # 登録確認用
                sql_2 = "SELECT * FROM favorite;"
                cursor.execute(sql_2)
                result = cursor.fetchall()

                for i in result:
                    print(i)
            
            connect.close()

    return render_template('favorite.html', favorites = result)