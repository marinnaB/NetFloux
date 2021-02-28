CREATE DATABASE baseCatalog;
use baseCatalog;

CREATE TABLE typesMovie (
  idType  MEDIUMINT NOT NULL AUTO_INCREMENT,
  nameType VARCHAR(100) NOT NULL,
  PRIMARY KEY (idType)
) ENGINE=InnoDB AUTO_INCREMENT=1;

CREATE TABLE movies (
  id MEDIUMINT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100),
  descriptionMovie VARCHAR(500),
  durationMin INT(10),
  imageMovie VARCHAR(500),
  idType MEDIUMINT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (idType) REFERENCES typesMovie(idType)
) ENGINE=InnoDB AUTO_INCREMENT=1;

CREATE TABLE myList (
  id MEDIUMINT NOT NULL AUTO_INCREMENT,
  idUser MEDIUMINT NOT NULL,
  idMovie MEDIUMINT NOT NULL,
  username VARCHAR(20),
  PRIMARY KEY (id),
  FOREIGN KEY (idMovie) REFERENCES movies(id)
) ENGINE=InnoDB AUTO_INCREMENT=1;

INSERT INTO typesMovie(nameType) VALUES ("Popular"), ("Action"), ("TV Shows"), ("Original");

INSERT INTO movies
  (title, descriptionMovie, durationMin, imageMovie, idType)
VALUES
  ("The Road Trick", "Description bla bla bbla", 125, '/static/images/1.PNG',1),
  ("Gray's Anatomy", "Description bla bla bbla", 125, '/static/images/2.PNG',2),
  ("Step up 2 The Streets", "Description bla bla bbla", 125, '/static/images/3.PNG',3),
  ("Wanted", "Description bla bla bbla", 130, '/static/images/4.PNG',4),
  
  ("The bourne ultimatum", "Description bla bla bbla", 150, '/static/images/5.PNG',1),
  ("Guardians of the galaxy", "Description bla bla bbla", 125, '/static/images/6.PNG',2),
  ("National tresor", "Description bla bla bbla", 130, '/static/images/7.PNG',3),
  ("Bad boys", "Description bla bla bbla", 150, '/static/images/8.PNG',4),
  
  ("Wynonna earp", "Description bla bla bbla", 125, '/static/images/9.PNG',1),
  ("Liquid science", "Description bla bla bbla", 130, '/static/images/10.PNG',2),
  ("The Vietnam war", "Description bla bla bbla", 150, '/static/images/11.PNG',3),
  ("The covenant", "Description bla bla bbla", 125, '/static/images/12.PNG',4),
  
  ("Riverdale", "Description bla bla bbla", 130, '/static/images/13.PNG',1),
  ("Queen of the south", "Description bla bla bbla", 150, '/static/images/14.PNG',2),
  ("Undercover boss", "Description bla bla bbla", 125, '/static/images/15.PNG',3),
  ("Penny dreadfull", "Description bla bla bbla", 130, '/static/images/16.PNG',4),
  
  ("The night shift", "Description bla bla bbla", 150, '/static/images/17.PNG',1),
  ("Hawai 50", "Description bla bla bbla", 125, '/static/images/18.PNG',2),
  ("The flash", "Description bla bla bbla", 130, '/static/images/19.PNG',3),
  ("Black lightning", "Description bla bla bbla", 150, '/static/images/20.PNG',4),
  
  ("New girl", "Description bla bla bbla", 125, '/static/images/21.PNG',1),
  ("The legend of tomorrow", "Description bla bla bbla", 125, '/static/images/22.PNG',2),
  ("Agence of shield", "Description bla bla bbla", 130, '/static/images/23.PNG',3),
  ("Marlon", "Description bla bla bbla", 150, '/static/images/24.PNG',4);

INSERT INTO myList
  (idUser, idMovie, username)
VALUES
  (1 , 10, 'test@yahoo.com'),
  (1 , 21, 'test@yahoo.com'),
  (1 , 9, 'test@yahoo.com');