CREATE DATABASE Monitor_de_noticias;
USE Monitor_de_noticias;

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





-- ================

-- tweets das paginas de noticias no twitter
create table tweet_paginas(pk_cod int auto_increment,
                           primary key(pk_cod),
                           nome varchar(100),
                           tweet varchar(1000),
                           data varchar(50))default charset=utf8;



-- Tweets de usuários
-- usuários aleatorios
create table user_aleatorio(
  pk_cod int auto_increment,
  primary key(pk_cod),
  nome varchar(50) unique not null
 )default charset=utf8;

-- usuarios que seguem as paginas
create table user_follow(pk_cod int auto_increment,
                         primary key(pk_cod),
                         nome varchar(50),
                         segue varchar(50))default charset=utf8;
                         

alter table tweets_follow add segue varchar(50);

-- usuarios que deram RT em alguma publicação das paginas
create table user_rt(pk_cod int auto_increment,
                     primary key(pk_cod),
                     nome varchar(50), 
                     rt_em_fk int,
                     foreign key(rt_em_fk) references tweet_paginas(pk_cod)
                     )default charset=utf8;   
                     

-- Tweets dos usuários
-- Aleatórios
create table tweets_aleatorio(user_nome varchar(50), 
                              tweet varchar(1000) unique not null, 
                              user_fk int,
                              foreign key(user_fk) references user_aleatorio(pk_cod),
                              data varchar(50)
                             )default charset=utf8;

-- Que seguem as paginas
create table tweets_follow(user_nome varchar(50), 
                           tweet varchar(1000), 
                           user_fk int, 
                           foreign key(user_fk) references user_follow(pk_cod),
                           data varchar(50)
                          )default charset=utf8;
                          
-- Que deram RT
create table tweets_rt(user_nome varchar(50), 
                       tweet varchar(1000), 
                       user_fk int,
                       foreign key(user_fk) references user_rt(pk_cod),
                       data varchar(50)
                      )default charset=utf8;


