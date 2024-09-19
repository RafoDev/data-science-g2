use db_codigo;

create table marca(
	id_marca int primary key auto_increment,
	nombre_marca varchar(50),
    pais_procedencia varchar(50)
);

insert into marca (nombre_marca, pais_procedencia) values
('Coca-cola', 'Estados Unidos'),
('PepsiCo', 'Estados Unidos'),
('Inca Kola', 'Perú'),
('Dr Pepper Snapple', 'Estados Unidos');

select * from marca;

create table gaseosa(
	id int primary key auto_increment,
    nombre varchar(50),
    precio float,
    id_marca int,
    foreign key (id_marca) references marca(id_marca)
);

insert into gaseosa(nombre, precio, id_marca) values 
('Coca-cola', 2.5, 1),
('Pepsi', 2.3, 2),
('Inca Kola', 2.4, 3),
('Fanta', 2.2, 1),
('Sprite', 2.2, 1); 

select * from marca;
select * from gaseosa;

-- inner join 

select * from gaseosa g 
inner join marca m
on g.id_marca = m.id_marca;

select * from gaseosa g
left join marca m
on g.id_marca = m.id_marca;

select * from gaseosa g
cross join marca m;

drop table marca;
drop table gaseosa;