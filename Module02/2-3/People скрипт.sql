DROP TABLE IF EXISTS people;
CREATE TABLE people(
   Person VARCHAR(17) NOT NULL 
  ,Region VARCHAR(27) NOT NULL
);
INSERT INTO people(Person,Region) VALUES ('Anna Andreadi','West');
INSERT INTO people(Person,Region) VALUES ('Chuck Magee','East');
INSERT INTO people(Person,Region) VALUES ('Kelly Williams','Central');
INSERT INTO people(Person,Region) VALUES ('Cassandra Brandow','South');