CREATE DATABASE IF NOT EXISTS rutes;
USE rutes;

CREATE TABLE ruta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alumne VARCHAR(255),
    descripcio TEXT,
    latitud DOUBLE,
    longitud DOUBLE
);

INSERT INTO ruta (alumne, descripcio, latitud, longitud) VALUES
('saulcespedes', 'Plaça de la Porxada', 41.6086, 2.2871),
('saulcespedes', 'Carrer de Joan Prim', 41.6062, 2.2846),
('saulcespedes', 'Carrer de Sant Roc', 41.6081, 2.2909),
('saulcespedes', 'Parc de la Franja', 41.6056, 2.2894),
('saulcespedes', 'Carrer de Josep Umbert', 41.6089, 2.2887);

Select * from ruta;
