-- Facebook database design

CREATE TABLE users(
    pk_user_id INT PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(200) NOT NULL ,
    last_name VARCHAR(200),
    gender VARCHAR(10),
    dob DATE,
    email VARCHAR(100) UNIQUE,
    mobileno VARCHAR (30) UNIQUE
    );

CREATE TABLE login(
    pk_login_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(200),
    password VARCHAR(200),
    fk_user_id INT,
    FOREIGN KEY(fk_user_id) REFERENCES users(pk_user_id)
    ON DELETE CASCADE ON UPDATE CASCADE
    );
    
CREATE TABLE friends(
    pk_friends_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_user_id INT,
    fk_friends_id INT,
    FOREIGN KEY(fk_user_id) REFERENCES users(pk_user_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(fk_friends_id) REFERENCES users(pk_user_id)
    ON DELETE CASCADE ON UPDATE CASCADE
    );

CREATE TABLE posts(
    pk_post_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_user_id INT,
    fk_image_id INT ,
    content VARCHAR (400),
    create_time DATETIME,
    FOREIGN KEY(fk_user_id) REFERENCES users(pk_user_id)
    ON DELETE CASCADE ON UPDATE CASCADE
    );


CREATE TABLE images(
    pk_img_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT, 
    img VARCHAR(100),
    is_profile BOOLEAN,
    FOREIGN KEY(post_id) REFERENCES psots(pk_post_id)
    ON DELETE CASCADE ON UPDATE CASCADE
    );


    
CREATE TABLE comments(
    pk_comment_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_post_id INT,
    comments VARCHAR (400),
    FOREIGN KEY(fk_post_id) REFERENCES posts(pk_post_id)
    ON DELETE CASCADE ON UPDATE CASCADE
    );

CREATE TABLE shares(
    pk_share_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_post_id INT,
    fk_friends_id INT,
    FOREIGN KEY(fk_post_id) REFERENCES posts(pk_post_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(fk_friends_id) REFERENCES friends(pk_friends_id)
    ON DELETE CASCADE ON UPDATE CASCADE
    );


CREATE TABLE likes(
    pk_like_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_post_id INT,
    fk_friends_id INT,
    FOREIGN KEY(fk_post_id) REFERENCES posts(pk_post_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(fk_friends_id) REFERENCES friends(pk_friends_id)
    ON DELETE CASCADE ON UPDATE CASCADE
    );


INSERT INTO users VALUES(null, 'Fname', 'Lname', 'male','2000-01=01', 'info@cybersquare.com', '9090767012');
INSERT INTO login VALUES(null, 'user', 'pass', 1);