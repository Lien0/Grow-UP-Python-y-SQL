CREATE TABLE sales (
  id INT GENERATED ALWAYS AS IDENTITY,
  product_id INT NOT NULL,
  quantity_sold INT NOT NULL DEFAULT 0,
  sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id),
  CONSTRAINT fk_product
  FOREIGN KEY(product_id)
  REFERENCES products(id)
  ON DELETE CASCADE 
);

INSERT INTO sales (product_id, quantity_sold) VALUES(1,4); 
INSERT INTO sales (product_id, quantity_sold) VALUES(2,5); 
INSERT INTO sales (product_id, quantity_sold) VALUES(3,9); 

SELECT
  p.category,
  SUM(s.quantity_sold) AS total_units_sold,
  SUM(p.price * s.quantity_sold) AS total_revenue
FROM products p
INNER JOIN sales s ON p.id = s.product_id
GROUP BY p.category
HAVING SUM(p.price * s.quantity_sold) > 100
ORDER BY total_revenue DESC;