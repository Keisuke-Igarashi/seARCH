#!/bin/sh
sudo docker stop search-web-1
sudo docker stop mysqldb
sudo docker rm search-web-1
sudo docker rm mysqldb
sudo docker rmi search-web
sudo docker rmi mysqldb
sudo docker compose -f docker-compose.yml up --build
