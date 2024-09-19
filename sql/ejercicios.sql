create table product(
	id int not null primary key auto_increment,	
	name varchar(200) not null,
    brand varchar(20) not null,
    price float
);

insert into product(name, brand, price) 
values 
('Ipad', 'Apple', 1700.0),
('Switch', 'Nintendo', 1400.0),
('PS5', 'Sony', 2400.0),
('Teclado', 'Logitech', 150.0),
('Mousepad', 'Logitech', 96.0),
('Hub', 'Ugreen', 67.0)
;

-- 1.1: Selecciona todos los productos cuyo “price” sea mayor a 500. Ordena los resultados por “price” de manera descendente.
SELECT * 
FROM product 
WHERE price > 500 
ORDER BY price DESC;

-- 1.2: Selecciona todos los productos de la marca "Logitech" y ordénalos alfabéticamente por name.
SELECT * 
FROM product
WHERE brand = 'Logitech' 
ORDER BY name ASC;

SELECT * 
FROM product
WHERE brand like 'Logi%' 
ORDER BY name ASC;

-- 1.3: Incrementa el precio en 10% para todos los productos de la marca "Apple".
UPDATE product
SET price = price * 1.10
WHERE id = 1;

UPDATE product
SET price = price * 1.10
WHERE brand = 'Apple';

-- 1.4: Selecciona todos los productos cuyo precio esté entre 100 y 1500, y ordénalos por brand.
SELECT * 
FROM product
WHERE price BETWEEN 100 AND 1500 
ORDER BY brand ASC;

-- 2.1: Contar el número de productos por marca
-- Utiliza group by para contar cuántos productos hay de cada marca.

select brand, count(*) as cantidad_productos
from product
group by brand;