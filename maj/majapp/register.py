import os
import json
import requests
import urllib.parse


from flask import (
    Blueprint, flash, render_template, request
)

from dotenv import load_dotenv


from majapp.db import get_db


bp = Blueprint('register', __name__)


@bp.route('/register', methods=('GET', 'POST'))
def register():

    # 初期変数設定
    result = ""
    architect_id = ""
    architecture_id = ""
    architect_name = ""
    architecture_name = ""
    postalcode = ""
    address1 = ""
    address2 = ""
    address3 = ""
    address4 = ""
    latitude = ""
    longitude = ""
    search_flg = ""
    result_architect_id = ""
    # 指定した建築家ID
    architect_id_used = ""

    if request.method == 'POST':

        # 建築家IDの取得
        try:
            architect_id = request.form['architect_id']
        except Exception as e:
            print(e)
            pass

        # 建築物名の取得
        try:
            architecture_name = request.form['architecture_name']
        except Exception as e:
            print(e)
            pass

        # 郵便番号の取得
        try:
            postalcode = request.form['postalcode']
        except Exception as e:
            print(e)
            pass

        # 住所1の取得
        try:
            address1 = request.form['address1']
        except Exception as e:
            print(e)
            pass

        # 住所2の取得
        try:
            address2 = request.form['address2']
        except Exception as e:
            print(e)
            pass
        
        # 住所3の取得
        try:
            address3 = request.form['address3']
        except Exception as e:
            print(e)
            pass

        # 住所4の取得
        try:
            address4 = request.form['address4']
        except Exception as e:
            print(e)
            pass

        # 緯度の取得
        try:
            latitude = request.form['latitude']
        except Exception as e:
            print(e)
            pass

        # 経度の取得
        try:
            longitude = request.form['longitude']
        except Exception as e:
            print(e)
            pass

        # コネクション取得
        connect = get_db()

        with connect.cursor() as cursor:

            sql = "INSERT INTO architecture \
            (architecture_name, postalcode, address1, address2, address3, address4, latitude, longitude, architect_id) \
            VALUES \
            (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(sql, (architecture_name, postalcode, address1, address2, address3, address4, latitude, longitude, architect_id, ))

        connect.commit()

        connect.close()

        result = '登録が完了しました'

        # # 建築家ＩＤの取得
        # if architect_name != "":

        #     with connect.cursor() as cursor:

        #         search_word = "%" + architect_name + "%"
        #         sql = "SELECT \
        #             architect_id \
        #             FROM architect \
        #             WHERE architect_name like %s;"

        #         cursor.execute(sql, (search_word, ))
        #         result_architect_id = cursor.fetchall()

        #         print(result_architect_id[0]['architect_id'])

        #         architect_id_used = result_architect_id[0]['architect_id']

        # Google map api呼び出し

        # load_dotenv('../env')
        # API_KEY = os.environ.get("API_KEY_GOOGLE_MAP")
        # print(API_KEY)

        # url_head = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="

        # url_search_word = urllib.parse.quote(architecture_name)

        # print(url_search_word)

        # url_keys = "&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key="

        # url = url_head + url_search_word + url_keys + API_KEY

        # payload={}
        # headers = {}

        # response = requests.request("GET", url, headers=headers, data=payload)

        # print(response.text)

    return render_template('register.html', registers=result)
