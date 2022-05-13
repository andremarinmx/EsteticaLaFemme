CREATE DATABASE LaFemme;

USE LaFemme;

CREATE TABLE trabajos(
    id_producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    precio INT NOT NULL,
    imagen VARCHAR(100),
    id_categoria INT NOT NULL
);

CREATE TABLE categorias(
    id_categoria INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL
);

ALTER TABLE trabajos
    ADD CONSTRAINT fk_id_categoria
    FOREIGN KEY (id_categoria)
    REFERENCES categorias(id_categoria);

CREATE TABLE usuarios(
    id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    contrasena VARCHAR(20) NOT NULL
);

INSERT INTO categorias(nombre) 
    VALUES('Cortes'),('Tintes'),('Productos');

INSERT INTO usuarios(nombre, contrasena)
    VALUES('admin', 'admin');