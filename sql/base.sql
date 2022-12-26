CREATE TABLE post(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(100)  NOT NULL
);

CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY,
    login VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    post INTEGER NOT NULL,
    FOREIGN KEY (post) REFERENCES post(id)
);

CREATE TABLE staff(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_user INTEGER NOT NULL,
  name VARCHAR(50) NOT NULL,
  surname VARCHAR(50) NOT NULL,
  id_post INTEGER NOT NULL,
  FOREIGN KEY (id_user) REFERENCES user(id),
  FOREIGN KEY (id_post) REFERENCES post(id)
);
CREATE TABLE shedule(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Data_race DATETIME NOT NULL,
  id_results INTEGER NOT NULL,
  id_race INTEGER NOT NULL,
  FOREIGN KEY (id_results) REFERENCES results(id),
  FOREIGN KEY (id_race) REFERENCES race(id)
);
CREATE TABLE race(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  length_distation VARCHAR(50) NOT NULL
);
CREATE TABLE racers(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  prize_place VARCHAR(50) NOT NULL,
  name VARCHAR(50) NOT NULL,
  surname VARCHAR(50) NOT NULL
);
CREATE TABLE results(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_racers INTEGER NOT NULL,
  id_shedule INTEGER NOT NULL,
  id_race INTEGER NOT NULL,
  total_time_race DATETIME NOT NULL,
  FOREIGN KEY (id_race) REFERENCES race(id),
  FOREIGN KEY (id_racers) REFERENCES racers(id),
  FOREIGN KEY (id_shedule) REFERENCES shedule(id)
);

INSERT INTO post(id,name) VALUES(1,'Manager');
INSERT INTO post(id,name) VALUES(2,'Engeener');
INSERT INTO post(id,name) VALUES(3,'Boss');
INSERT INTO post(id,name) VALUES(4,'Cleaner');

INSERT INTO users(id, login, password, post) VALUES (1, 'Manager', 'admin', 1);
INSERT INTO users(id, login, password, post) VALUES (2, 'Max', 'admin1', 2);
INSERT INTO users(id, login, password, post) VALUES (3, 'Dan', 'admin2', 3);
INSERT INTO users(id, login, password, post) VALUES (4, 'Chris', 'admin3', 4);

INSERT INTO staff(id_user, name,surname,id_post) VALUES (1,'Maxim', 'Rybnikov',1);
INSERT INTO staff(id_user, name,surname,id_post) VALUES (2, 'Denzel', 'Dumpfries',2);
INSERT INTO staff(id_user, name,surname,id_post) VALUES (3, 'Christian', 'Eriksen',3);
INSERT INTO staff(id_user, name,surname,id_post) VALUES (4, 'Julian', 'Draxler',4);

INSERT INTO shedule (Data_race, id_results,id_race) VALUES ('2007-03-10',1,1);
INSERT INTO shedule (Data_race, id_results,id_race) VALUES ('2006-07-11',2,2);
INSERT INTO shedule (Data_race, id_results,id_race) VALUES ('2008-06-11',3,3);
INSERT INTO shedule (Data_race, id_results,id_race) VALUES ('2005-02-10',4,4);

INSERT INTO race(name, length_distation) VALUES ('Gran-Pri USA','200 km');
INSERT INTO race(name, length_distation) VALUES ('Gran-Pri Monaco','150 km');
INSERT INTO race(name, length_distation) VALUES ('Gran-Pri Spain','305 km');
INSERT INTO race(name, length_distation) VALUES ('Gran-Pri Portugal','250 km');

INSERT INTO racers(prize_place,name,surname) VALUES('1','Markus','Rashford');
INSERT INTO racers(prize_place,name,surname) VALUES('2','Lukas','Hradecky');
INSERT INTO racers(prize_place,name,surname) VALUES('3','Lucas','Moura');
INSERT INTO racers(prize_place,name,surname) VALUES('4','Cody','De Winter');

INSERT INTO results(id_racers, id_shedule,id_race,total_time_race) VALUES (1,1,1,'1:30:22');
INSERT INTO results(id_racers, id_shedule,id_race,total_time_race) VALUES (2,2,2,'1:35:29');
INSERT INTO results(id_racers, id_shedule,id_race,total_time_race) VALUES (3,3,3,'1:39:46');
INSERT INTO results(id_racers, id_shedule,id_race,total_time_race) VALUES (4,4,4,'1:40:27');