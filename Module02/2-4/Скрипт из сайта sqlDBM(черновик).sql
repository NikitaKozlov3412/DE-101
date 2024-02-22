-- ************************************** Ludi

CREATE TABLE Ludi
(
 Region varchar(15) NOT NULL,
 Person varchar(30) NOT NULL

);

-- ************************************** Vozvraty

CREATE TABLE Vozvraty
(
 "Order ID" varchar(25) NOT NULL,
 Returned varchar(30) NOT NULL

);


-- ************************************** Tablica
drop table if exists tablica ;
CREATE TABLE Tablica
(
 Row_ID      integer NOT NULL,
 "Order Date"  date NOT NULL,
 "Customer ID" varchar(25) NOT NULL,
 Country     varchar(25) NOT NULL,
 City        varchar(25) NOT NULL,
 "State"       varchar(25) NOT NULL,
 "Product ID"  varchar(25) NOT NULL,
 Sales       numeric(9,4) NOT NULL,
 Ship_id      varchar(30) NOT NULL,
 Person      varchar(30) NOT NULL,
 Returned    varchar(30) NOT NULL,
 Region_1    varchar(15) NOT NULL,
 "Order ID_1"  varchar(25) NOT NULL

);

CREATE INDEX FK_1 ON Tablica
(
 "Order ID_1"
);

CREATE INDEX FK_2 ON Tablica
(
 Region_1
);

select * from ludi ;
select * from vozvraty ;
select * from tablica ;

select *
from tablica left join ludi on tablica.region_1 = ludi.region;

select *
from vozvraty v2 right join tablica on tablica."Order ID_1" = v2."Order ID";

select *
from tablica left join orders on tablica.region_1 = orders.region;

select * 
from orders left join tablica on orders.region = tablica.region_1;



--creating a table
drop table if exists ship ;
CREATE TABLE ship
(
  ship_id SERIAL NOT NULL,
  ship_mode VARCHAR(14) NOT NULL,
  
  CONSTRAINT PK_ship PRIMARY KEY (ship_id)
);

-- deleting rows
TRUNCATE TABLE ship;

-- inserting data from orders
INSERT INTO ship (ship_mode)
SELECT distinct ship_mode
from orders;

-- checking
select 	* FROM  ship;

-- не работает скрипт

insert into tablica 
 (Ship_id)
SELECT DISTINCT 
	s.ship_id
	from orders AS o 
inner join ship s on o.ship_mode = s.ship_mode;

