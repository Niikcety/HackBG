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

SELECT starname
  FROM STARSIN
  JOIN MOVIESTAR ON STARSIN.starname = MOVIESTAR.name
  WHERE movietitle = "Terms of Endearment" and gender = "M"

SELECT starname
  FROM STARSIN
  JOIN MOVIE ON STARSIN.movietitle = MOVIE.TITLE
  WHERE studioname = "MGM" and year = 1995

ALTER TABLE STUDIO
  ADD president_name TEXT

UPDATE STUDIO
  SET president_name = "Bob Chapek"
  WHERE name = "Disney"

UPDATE STUDIO
  SET president_name = "Gary Ehrlich"
  WHERE name = "Fox"

UPDATE STUDIO
  SET president_name = "Bill Hornbuckle"
  WHERE name = "MGM"

UPDATE STUDIO
  SET president_name = "Jim Gianopulos"
  WHERE name = "Paramount"

UPDATE STUDIO
  SET president_name = "John Johnson"
  WHERE name LIKE "USA%"

UPDATE STUDIO
  SET president_name = "Ann Sarnoff"
  WHERE name = "Warner Bros"

SELEct president_name
  FROM STUDIO
  WHERE name = "MGM"