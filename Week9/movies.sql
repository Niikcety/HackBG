SELECT address
  FROM STUDIO
  WHERE name = "MGM"

SELECT birthdate
  FROM MOVIESTAR
  WHERE name = "Kim Basinger"

SELECT name
  FROM MOVIEEXEC
  WHERE networth >= 10000000;

SELECT name
  FROM MOVIESTAR
  WHERE gender = "M" or address = "Prefect Rd%";

Insert INTO MOVIESTAR
  VALUES("Zahari Baharov", "Zahari Baharov's str", "M", "1980-05-04");

DELETE FROM STUDIO
  WHERE address LIKE "%5%";

UPDATE MOVIE
  SET studioname = "FOX"
  WHERE title LIKE "%star%";
