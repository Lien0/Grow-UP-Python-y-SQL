CREATE DATABASE stitch_store_db;
/*Importante usar USE para aclarar en que BD vmaos a trabajar*/
USE stitch_store_db;

CREATE TABLE products (
    id int NOT NULL GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    /*No es necesario aclarar UNIQUE si lo voy a colocar como Primary Key*/
    -- UNIQUE(id),
    PRIMARY KEY(id)
);

INSERT INTO products (name,category, price, stock_quantity) 
VALUES (
    /*Se utilizan comillas simples para cadenas de texto
    Solo se usan comillas dobles o backticks `` para nombre de tablas o columnas*/
    'Navbar',
    'UI Desing',
    25.20,
    2
);

INSERT INTO products (name,category, price, stock_quantity) 
VALUES (
    'Footer',
    'UI Desing',
    57.20,
    5
);

INSERT INTO products (name,category, price, stock_quantity) 
VALUES (
    'Dashboard Layout',
    'UX Desing',
    88.30,
    6
);

/*Lo correcto es usar los nombres de columnas sin paréntesis*/
SELECT name, price FROM products 
WHERE price > 50.00 ORDER BY price DESC;