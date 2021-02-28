CREATE DATABASE myBase;
use myBase;

CREATE TABLE users (
  id MEDIUMINT NOT NULL AUTO_INCREMENT,
  username VARCHAR(20),
  pwd VARCHAR(500),
  token VARCHAR(200),
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO users
  (username, pwd)
VALUES
  ('titi@yahoo.com', 'pbkdf2:sha256:150000$JT7Nf8kh$14e5f48c4a5c202a818b8c1595f150362501896bb17ced6bc252626d29fe696b'),
  ('test@yahoo.com', 'pbkdf2:sha256:150000$ZMy3wuxp$15f3c0e1ab558935b5cafd903cf64342ccc0ecc18c75aa7b32f3bce35e9e16e9');