# Docker image
FROM mysql

# port
EXPOSE 3306

# copy my.cnf
COPY ./my.cnf /etc/mysql/conf.d/my.cnf

# docker run時の実行コマンド
CMD [ "mysqld" ]