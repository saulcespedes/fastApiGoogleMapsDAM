CREATE DATABASE IF NOT EXISTS nombre_de_tu_base_de_datos;
USE nombre_de_tu_base_de_datos;

CREATE TABLE ruta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alumne VARCHAR(255),
    descripcio TEXT,
    latitud DOUBLE,
    longitud DOUBLE
);
