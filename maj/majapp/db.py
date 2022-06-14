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

    return connect