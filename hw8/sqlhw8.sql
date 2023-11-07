show databases;
create database test;
use test;

create table users (
  name varchar(255) primary key,
    password varchar(255) not null
);

insert into test.`users` values('Alua', 'alua');
insert into users values('Ali', 'ali');
insert into users values('Jandaulet', 'jandaulet');
insert into users values('Ayau', 'ayau');
insert into users values('Bota', 'akbota');

select * from users;
