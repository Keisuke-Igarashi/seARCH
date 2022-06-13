#!/bin/bash
# 建物情報登録用シェル

echo "[INFO] 処理開始"
MYSQL_SCHEMA="majdb"
ROOT_DIRECTORY="/Docker/mysql/"
CMD_MYSQL="mysql --defaults-extra-file=$ROOT_DIRECTORY/mysql.conf -t --show-warnings $MYSQL_SCHEMA"