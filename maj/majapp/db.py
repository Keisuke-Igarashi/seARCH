import pymysql.cursors

def get_db():
    connect = pymysql.connect(
                            host="mysqldb",
                            # port=3306,
                            user='root',
                            password='p@ssw0rd',
                            db='majdb',
                            cursorclass=pymysql.cursors.DictCursor

    )

    with connect.cursor() as cursor:
        sql = "SELECT * FROM architect"
        cursor.execute(sql)
        result= cursor.fetchall()

    connect.close()
    return result