CREATE DATABASE LaFemme;

USE LaFemme;

CREATE TABLE trabajos(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    precio float NOT NULL
);