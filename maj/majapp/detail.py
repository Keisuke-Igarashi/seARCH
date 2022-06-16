from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, make_response
)

import ast
import json

from majapp.db import get_db

bp = Blueprint('detail', __name__)

@bp.route('/detail', methods=('GET', 'POST'))
def detail():

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

                # 建物の全情報を取得する
                sql_2 = "SELECT * FROM architecture WHERE architecture_id = %s;"
                cursor.execute(sql_2,(architecture_id,))
                result = cursor.fetchall()

                # for i in result:
                #     print(i)
            
            connect.close()

            # response = make_response(render_template('detail.html', details = result))

            # print(response)
            # print(type(response))
            # redirect('/detail', code=302)

    return render_template('detail.html', details = result)