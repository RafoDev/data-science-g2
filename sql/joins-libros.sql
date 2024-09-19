-- Crear la tabla de autor
CREATE TABLE autor (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

-- Insertar datos en la tabla de autor
INSERT INTO autor (nombre, apellido) VALUES
('Ellen', 'Writer'),
('Olga', 'Savelieva'),
('Jack', 'Smart'),
('Donald', 'Brain'),
('Yao', 'Dou');

-- Crear la tabla de editor
CREATE TABLE editor (
    id_editor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

-- Insertar datos en la tabla de editor
INSERT INTO editor (nombre, apellido) VALUES
('Daniel', 'Brown'),
('Mark', 'Johnson'),
('María', 'Evans'),
('Catherine', 'Roberts'),
('Sebastián', 'Wright'),
('Bárbara', 'Jones'),
('Mateo', 'Smith');

-- Crear la tabla de traductor
CREATE TABLE traductor (
    id_traductor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

-- Insertar datos en la tabla de traductor
INSERT INTO traductor (nombre, apellido) VALUES
('Ira', 'Davies'),
('Ling', 'Weng'),
('Kristian', 'Green'),
('Roman', 'Edwards');

-- Crear la tabla de libro
CREATE TABLE libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    tipo ENUM('original', 'traducido'),
    id_autor INT,
    id_editor INT,
    id_traductor INT,
    FOREIGN KEY (id_autor) REFERENCES autor(id_autor),
    FOREIGN KEY (id_editor) REFERENCES editor(id_editor),
    FOREIGN KEY (id_traductor) REFERENCES traductor(id_traductor)
);

-- Insertar datos en la tabla de libro
INSERT INTO libro (titulo, tipo, id_autor, id_editor, id_traductor) VALUES
('¡Es hora de crecer!', 'original', 1, 1, NULL),
('Tu Viaje', 'traducido', 5, 2, 2),
('Amor Encantador', 'original', 4, 4, NULL),
('Sueña Tu Vida', 'original', 1, 4, NULL),
('Naranjas', 'traducido', 2, 5, 1),
('Tu Vida Feliz', 'traducido', 5, 2, 3),
('IA Aplicada', 'traducido', 3, 3, 4),
('Mi Último Libro', 'original', 1, 7, NULL);



-- 1. Mostrar los títulos de los libros junto con sus autores (nombre y apellido).
-- ¿Cuál sería la query?

-- libro y autor

select l.titulo, a.nombre as nombre_autor, a.apellido from 
libro l inner join autor a 
on l.id_autor = a.id_autor;

-- 2. Mostrar los libros con sus traductores,
-- cols: l.id, l.titulo, l.tipo, t.apellido
-- ¿Cuál sería la query?

select l.id, l.titulo, l.tipo, t.apellido as traductor from 
libro l inner join traductor t
on l.id_traductor = t.id_traductor;

-- 3. Mostrar información sobre el autor y el traductor de cada libro
-- apellidos y tambien mantener la información básica de cada libro (id, titulo, tipo)
-- ¿Cuál sería la query?

select l.id, l.titulo, l.tipo, a.apellido as autor, t.apellido as traductor from 
libro l left join autor a
on l.id_autor = a.id_autor
left join traductor t
on l.id_traductor = t.id_traductor;

create view view_libros_completos as 
select 
	l.id,
    l.titulo,
    l.tipo,
    concat(a.nombre,' ', a.apellido) as autor,
    concat(e.nombre,' ', e.apellido) as editor,
    concat(t.nombre,' ', t.apellido) as traductor
from libro l
left join autor a on l.id_autor = a.id_autor
left join traductor t on l.id_traductor = t.id_traductor
left join editor e on l.id_editor = e.id_editor;

select * from view_libros_completos where tipo = 'traducido';
