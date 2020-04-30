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
