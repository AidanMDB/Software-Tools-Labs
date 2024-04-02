CREATE TABLE users (
    username text,
    gender text,
    age int,
    userid int PRIMARY KEY
);

CREATE TABLE posts (
    content text,
    posttitle text,
    postid int,
    userid int
);

INSERT INTO users (username, gender, age, userid) VALUES
    ('aidan', 'male', 20, 1536),
    ('bob', 'male', 34, 16234),
    ('god', 'Andro', 100000, 896123),
    ('emma', 'female', 25, 12398),
    ('lando', 'male', 40, 2348876);

INSERT INTO posts (content, posttitle, postid, userid) VALUES
    ('This is my first posts', 'First Title', 1, 1536),
    ('I love my job', 'JOB', 2, 1536),
    ('ALL HAIL', 'Scipture', 1, 896123),
    ('lulu lemon', 'Favorite Store', 1, 12398),
    ('I own the millenium falcon', 'Star Wars', 1, 2348876),
    ('No matching userid', 'title', 1, 1209);

SELECT users.userid, users.username, users.age, posts.posttitle
FROM users
CROSS JOIN posts;

DROP TABLE users;
DROP TABLE posts;