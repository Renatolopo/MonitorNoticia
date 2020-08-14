CREATE DATABASE Monitor_de_noticias;
use Monitor_de_noticias;

CREATE TABLE veja(
ID int not null auto_increment,
TITULO varchar(255) not null unique,
DESCRICAO varchar(5000),
HORARIO varchar(255),
primary key(ID)
) default charset=utf8;


CREATE TABLE G1(
ID int not null auto_increment,
TITLE varchar(1000) not null unique, 
LINK varchar(1000), 
SUMMARY varchar(5000), 
PUBLISHED varchar(255),
primary key(ID)
)default charset=utf8;


CREATE TABLE R7(
ID int not null auto_increment,
TITLE varchar(1000) not null unique, 
LINK varchar(1000), 
SUMMARY varchar(5000), 
PUBLISHED varchar(255),
primary key(ID)
)default charset=utf8;

CREATE TABLE Folha(
ID int not null auto_increment,
TITLE varchar(1000) not null unique, 
LINK varchar(1000), 
SUMMARY varchar(5000), 
PUBLISHED varchar(255),
primary key(ID)
)default charset=utf8;

CREATE TABLE Sbt(
ID int not null auto_increment,
TITLE varchar(1000) not null unique, 
SUBTITLE varchar(1000) not null, 
PUBLISHED varchar(255),
primary key(ID)
)default charset=utf8;

CREATE TABLE Twitter(
ID INT NOT NULL auto_increment,
USUARIO VARCHAR(255),
TWEET VARCHAR(1000) not null unique,
DATA_TWEET VARCHAR(255),
primary key(ID)
)default charset=utf8;

