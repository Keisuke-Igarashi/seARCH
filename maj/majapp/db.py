import pymysql.cursors
# import mysql.connector


def get_db():
    connect = pymysql.connect(
                            host="mysqldb",
                            # port=3306,
                            user='root',
                            password='password',
                            db='majdb',
                            cursorclass=pymysql.cursors.DictCursor
    )
    # connect = mysql.connector.connect(
    #                         host="mysqldb",
    #                         # port=3306,
    #                         user='root',
    #                         password='password',
    #                         database='majdb',
    #                         auth_plugin='mysql_native_password',
    #                         charset='utf8mb4',
    # )

    return connect
