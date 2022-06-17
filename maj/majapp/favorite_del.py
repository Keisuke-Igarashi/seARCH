from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

import ast
import json

from majapp.db import get_db

bp = Blueprint('favorite_del', __name__)

@bp.route('/favorite_del', methods=('GET', 'POST'))
def favorite():

    result = ""
    result2 = ""
    
    if request.method == 'POST':
        
        architecture_id = request.form['architecture_id']

        error = None

        if not architecture_id:
            error = 'architecture_id is required.'

        if error is not None:
            flash(error)

        else:
          
            # result2 = architecture_id
            connect = get_db()

            with connect.cursor() as cursor:
          
                # お気に入りデータを更新する
                sql_1 = " DELETE FROM favorite WHERE architecture_id = %s;"
                cursor.execute(sql_1,(architecture_id,))
                
            connect.commit()
            
            with connect.cursor() as cursor:

                # 登録確認用
                sql_2 = "SELECT \
                            fav.architecture_id, \
                            arch.architect_id, \
                            c.architect_name, \
                            arch.architecture_name, \
                            arch.postalcode, \
                            arch.address1, \
                            arch.address2, \
                            arch.address3, \
                            arch.address4 \
                        FROM favorite as fav \
                        JOIN architecture as arch \
                        ON fav.architecture_id = arch.architecture_id \
                        JOIN architect as c \
                        ON arch.architect_id = c.architect_id \
                        ORDER BY fav.createdate DESC\
                        ;"
                cursor.execute(sql_2)
                result = cursor.fetchall()

                # for i in result:
                #     print(i)

            connect.close() 
    
    else:
        connect = get_db()
        
        with connect.cursor() as cursor:

            # 登録確認用
            sql_2 = "SELECT \
                        fav.architecture_id, \
                        arch.architect_id, \
                        c.architect_name, \
                        arch.architecture_name, \
                        arch.postalcode, \
                        arch.address1, \
                        arch.address2, \
                        arch.address3, \
                        arch.address4 \
                    FROM favorite as fav \
                    JOIN architecture as arch \
                    ON fav.architecture_id = arch.architecture_id \
                    JOIN architect as c \
                    ON arch.architect_id = c.architect_id \
                    ORDER BY fav.createdate DESC\
                    ;"
            cursor.execute(sql_2)
            result = cursor.fetchall()


    return render_template('favorite.html',  favorites = result)