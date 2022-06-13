# Docker image
FROM mysql:debian

# port
EXPOSE 3306

# copy 初回実行sql
COPY ./initdb.d/* /docker-entrypoint-initdb.d/

# copy my.cnf
COPY ./my.cnf /etc/mysql/conf.d/my.cnf

# docker run時の実行コマンド
CMD [ "mysqld" ]