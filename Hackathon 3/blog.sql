DROP DATABASE IF EXISTS blog_log;

CREATE DATABASE IF NOT EXISTS blog_log;

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    password VARCHAR(255)
) ENGINE=InnoDB ;

CREATE TABLE IF NOT EXISTS posts (
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    content VARCHAR(255),
    author INT,
    created timestamp default now()
) ENGINE=InnoDB ;

ALTER TABLE posts
ADD FOREIGN KEY (author) REFERENCES users(id);
