-- DML: DATA MANIPULATION LANGUAGE
-- CRUD: CREATE-READ-UPDATE-DELETE

-- insertar registro
insert into alumno(nombre, email, celular, nota) 
value ('Rafael', 'rafael.david@gmail.com', '948373283', 13);

-- insertar múltiples registros
insert into alumno(nombre, email, celular, nota)
values 
('luis', 'luis@gmail.com', '23232342',15),
('maria', 'maria@gmail.com', '5332342',11),
('jose', 'jose@gmail.com', '67232342',20),
('pedro', 'pedro@gmail.com', '236432342',13),
('carmen', 'carmen@gmail.com', '23862342',05)
;

-- mostrar

select * from alumno;
select * from alumno limit 2;
select nombre, email from alumno;

select nombre, nota from alumno order by nota asc;

select nombre, nota from alumno order by nota desc;

select nombre, nota from alumno where nota >= 15;

-- Una consulta que muestre los registros con notas entre
-- (15 - 11)

select nombre, nota from alumno where nota >= 11 and nota <= 15;
select nombre, nota from alumno where nota between 11 and 15;

select email from alumno where email like '%gmail%';

select max(nota) as mayor_nota from alumno;
select min(nota) as menor_nota from alumno;
select avg(nota) as nota_promedio from alumno;
select count(*) as total_alumnos from alumno;

-- actualizar datos
update alumno 
set celular = "999999"
where id = 1;

-- Error Code: 1175. 
-- You are using safe update mode and you tried to update a 
-- table without a WHERE that uses a KEY column.  
-- To disable safe mode, toggle the option in Preferences -> 
-- SQL Editor and reconnect.

-- eliminar datos
delete from alumno where id = 7;

select * from alumno;

-- numero de duplicados
select nombre, celular, email, nota, count(*) as ocurrencias
from alumno
group by nombre, celular, email, nota;



