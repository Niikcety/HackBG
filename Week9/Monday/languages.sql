CREATE TABLE languages(
  id INTEGER PRIMARy KEY,
  language VARCHAR(20),
  answer TEXT,
  answered INTEGER,
  guide TEXT
);

INSERT INTO languages
  VALUES(1, "Python", "google", 0, "A folder named Python was created. Go there ");
INSERT INTO languages
  VALUES(2, "Go", "200 OK", 0, "A folder named Go was created. Go there and try to make Google Go run.");
INSERT INTO languages
  VALUES(3, "Java", "object oriented programming", 0, "A folder named Java was created. Can you handle the class?");
INSERT INTO languages
  VALUES(4, "Haskell", "Lambda", 0, "Something pure has landed. Go to Haskell folder and see it!");
INSERT INTO languages
  VALUES(5, "C#", "NDI=", 0, "Do you see sharp? Go to the C# folder and check out.");
INSERT INTO languages
  VALUES(6, "Ruby", "https://www.ruby-lang.org//bg/", 0 , "Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!");
INSERT INTO languages
  VALUES(7, "C++", "header file", 0, "Here be dragons! It's C++ time. Go to the C++ folder.");
INSERT INTO languages
  VALUES(8, "JavaScript", "Douglas Crockford", 0, "NodeJS time. Go to JavaScript folder and Node your way!");


ALTER TABLE languages
  ADD COLUMN rating INTEGER  CHECK(rating > 0 AND rating < 10);


Update languages
  SET rating = 9
  WHERE language = "Python" 

Update languages
  SET rating = 6
  WHERE language = "Go" 

UPDATE languages
  SET rating = 8
  WHERE language = "Java"

UPDATE languages
  SET rating = 5
  WHERE language = "Haskell" 

UPDATE languages
  SET rating = 3
  WHERE language = "C#" 

UPDATE languages
  SET rating = 4
  WHERE language = "Ruby" 

UPDATE languages
  SET rating = 9
  WHERE language = "C++" 

UPDATE languages
  SET rating = 6
  WHERE language = "JavaScript" 

UPDATE languages
  SET answered = 1
  WHERE language = "Python" or language = "Go";

SELECT *
  FROM languages
  WHERE answer = "200 OK" or answer = "Lambda";