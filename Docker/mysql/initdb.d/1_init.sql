DROP DATABASE IF EXISTS majdb;
CREATE DATABASE majdb;
USE majdb;
DROP TABLE IF EXISTS architecture;


CREATE TABLE architecture
(
    architecture_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    architecture_name VARCHAR(100) NOT NULL,
    postalcode CHAR(10) NOT NULL,
    address1 VARCHAR(100) NOT NULL,
    address2 VARCHAR(100) NOT NULL,
    address3 VARCHAR(100) ,
    address4 VARCHAR(100) ,
    latitude FLOAT(20,15) NOT NULL,
    longitude FLOAT(20,15) NOT NULL,
    architect_id INT NOT NULL,
    createdate DATETIME DEFAULT CURRENT_TIMESTAMP,
    updatedate DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP


);

DROP TABLE IF EXISTS architect;


CREATE TABLE architect
(
    architect_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    architect_name CHAR(100) NOT NULL,
    createdate DATETIME DEFAULT CURRENT_TIMESTAMP

);

DROP TABLE IF EXISTS favorite;

CREATE TABLE favorite
(
    favorite_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    architecture_id INT NOT NULL,
    createdate DATETIME DEFAULT CURRENT_TIMESTAMP

);

DROP TABLE IF EXISTS user;


CREATE TABLE user
(
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_name CHAR(50) NOT NULL,
    password CHAR(50) NOT NULL,
    createdate datetime, 
    updatedate datetime
);