-- DDL - Data definition Language
-- crear la base de datos
create database db_codigo;
show databases;
use db_codigo;

-- crear primera tabla
create table alumno(
	id int not null primary key auto_increment,	
	nombre varchar(200) not null,
    celular varchar(20),
    email varchar(100)
);

-- para añadir un campo
ALTER TABLE alumno ADD COLUMN nota INT;

-- borrar la tabla
drop table alumno;
-- mostrar la query de creación de la tabla
show create table alumno;