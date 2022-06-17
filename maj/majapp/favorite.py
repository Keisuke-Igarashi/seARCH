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
    architecture_id = ""
    architect_name = ""
    architecture_name = ""
    address1 = ""
    search_flg = ""
    
    if request.method == 'POST':
        
        # print('!!!!!!!!!!!!!!!!!!!はいった!!!!!!!!!!!!!!!!')

        # jsから受け取った変数

        if(request.data):
            param = json.loads(request.data.decode('utf-8'))
            print(param)
        
            architecture_id = param['architecture_id']

        # 検索窓から受け取った変数
        try:
            print('!!!!!!!!!!!!!!!!!!!はいった!!!!!!!!!!!!!!!!')
            architect_name = request.form['architect_name']
            print('!!!!!!!!!!!!!'+architect_name+'!!!!!!!!!!!!!')
        except:
            pass

        try:
            architecture_name = request.form['architecture_name']
        except:
            pass

        try:
            address1 = request.form['address1']
        except:
            pass
        
        try:
            search_flg = request.form['search_flg']
            print('!!!!!!!!!!!!!!!!!!!はいった!!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!!!!'+search_flg+'!!!!!!!!!!!!!')
        except:
            pass
        
        
        error = None

        # if not architecture_id:
        #     error = 'architecture_id is required.'

        if error is not None:
            flash(error)

        else:
          
            # result2 = architecture_id
            connect = get_db()

            # jsからのお気に入り登録をダブルクリックで受け取る処理
            if(architecture_id != '' and search_flg != "True"):

                print('!!!!!!!!!!!!!!!!!!!はいった!!!!!!!!!!!!!!!!')

                with connect.cursor() as cursor:
            
                    # お気に入りデータを登録する
                    sql_1 = "INSERT INTO favorite (user_id, architecture_id) VALUES (%s, %s);"
                    cursor.execute(sql_1,('1', architecture_id,))
                    
                connect.commit()

            # 建築家名の検索条件を受け取ってsql実行する処理
            elif(architect_name != "" and search_flg == "True"):

                print('!!!!!!!!!!!!!!!!!!!はいった!!!!!!!!!!!!!!!!')

                with connect.cursor() as cursor:

                    # 建築家名で検索
                    search_word = "%" + architect_name + "%"
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
                    WHERE c.architect_name like %s \
                    ORDER BY fav.createdate DESC\
                    ;"
                    cursor.execute(sql_2,(search_word,))
                    result = cursor.fetchall()

            # 建物名の検索条件を受け取ってsql実行する処理
            elif(architecture_name != "" and search_flg == "True"):

                with connect.cursor() as cursor:

                    # 建物名で検索
                    search_word = "%" + architecture_name + "%"
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
                    WHERE arch.architecture_name like %s \
                    ORDER BY fav.createdate DESC\
                    ;"
                    cursor.execute(sql_2,(search_word,))
                    result = cursor.fetchall()

            # 都道府県名の検索条件を受け取ってsql実行する処理
            elif(address1 != "" and search_flg == "True"):

                with connect.cursor() as cursor:

                    # 都道府県で検索
                    search_word = "%" + address1 + "%"
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
                    WHERE arch.address1 like %s \
                    ORDER BY fav.createdate DESC\
                    ;"
                    cursor.execute(sql_2,(search_word,))
                    result = cursor.fetchall()           
            
            connect.close()

        # GETの場合(一覧表示用)
    else:

        # result2 = architecture_id
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

            # for i in result:
            #     print(i)
        
        connect.close()


    return render_template('favorite.html', favorites = result)