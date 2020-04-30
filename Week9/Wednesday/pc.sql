SELECT AVG(speed) 
FROM pc;

SELECT AVG(screen) AS "Average screen size", Maker 
FROM laptop 
JOIN product 
ON product.model = laptop.model 
GROUP BY maker 

SELECT AVG(speed) 
FROM laptop
WHERE price > 1000  

SELECT AVG(price), hd 
FROM pc 
GROUP BY hd 

SELECT AVG(price), speed 
FROM pc 
GROUP BY speed 
HAVING speed > 500

SELECT AVG(price) 
FROM pc 
JOIN product 
ON product.model = pc.model 
WHERE maker = 'A'

SELECT AVG(price) 
FROM (SELECT AVG(price) AS price 
	  FROM laptop 
	  JOIN product 
	  ON laptop.model = product.model 
	  GROUP BY maker 
	  HAVING maker = 'B' 
	  UNION 
	  SELECT AVG(price) AS price 
	  FROM pc 
	  JOIN product 
	  ON pc.model = product.model 
	  GROUP BY maker 
	  HAVING maker = 'B')

SELECT maker 
   FROM (SELECT COUNT(maker) as number, maker 
   FROM PRODUCT 
   WHERE TYPE = "PC" 
   GROUP BY maker) 
   WHERE NUMBER >= 3; 

SELECT maker 
FROM (SELECT price, maker 
	  FROM pc 
	  JOIN product 
	  ON pc.model = product.model 
	  GROUP BY maker 
	  ORDER BY price DESC) 
LIMIT 1

SELECT AVG(hd) 
   FROM pc 
   JOIN product  
   ON product.model = pc.model 
   WHERE maker = (SELECT maker  
          FROM pc  
          JOIN product  
          ON pc.model = product.model  
          WHERE maker = (SELECT maker  
                         FROM printer  
                         JOIN product  
                         ON printer.model = product.model)  
          GROUP BY maker);  
