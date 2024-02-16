select sum(sales) as revenue from orders o 
/*WHERE order_date > '2016-01-01' and order_date < '2016-01-31';*/
where extract ('year' from order_date) = 2016;
select sum(sales) as revenue from orders o 
where extract ('year' from order_date) = 2016 and extract ('month' from order_date) = 12;
select sum(sales) as revenue from orders o 
where extract ('year' from order_date) = 2018;
select sum(sales) as revenue from orders o 
where extract ('year' from order_date) = 2019;