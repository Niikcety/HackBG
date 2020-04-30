SELECT name, country, numguns, launched 
  FROM SHIPS 
    JOIN CLASSES 
      ON ships.class = classes.class; 

--

SELECT ships.name 
          FROM OUTCOMES 
          JOIN BATTLES 
          ON OUTCOMES.BATTLE = BATTLES.NAME 
          JOIN SHIPS 
          ON OUTCOMES.SHIP = SHIPS.NAME 
          WHERE DATE LIKE "1942%";    


SELECT country, name 
          FROM SHIPS 
          JOIN CLASSES 
          ON SHIPS.CLASS = CLASSES.CLASS 
          WHERE name NOT IN ( SELECT ship 
                              FROM OUTCOMES) 
          ORDER BY country; 