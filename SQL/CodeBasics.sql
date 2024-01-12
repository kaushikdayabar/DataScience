/*year wise sales*/ 
Select dt.year,Sum(sales_amount) as "Total Sales" from sales.transactions as t inner join sales.date as dt on t.order_date=dt.date group by dt.year;

/*region wise sales*/
Select m.markets_code,m.markets_name,SUM(t.sales_amount) as "Total Sales" from sales.markets as m inner join sales.transactions as t on m.markets_code=t.market_code group by m.markets_code order by Sum(t.sales_amount) ; 

/*product wise sales above 1 crore*/
Select p.product_code,sum(t.sales_amount) as "Total Sales" from sales.products as p inner join sales.transactions as t on p.product_code=t.product_code group by p.product_code having  sum(t.sales_amount)>10000000 order by sum(t.sales_amount); 

/*Customer type wise sales*/
Select c.customer_type,Sum(t.sales_amount) from sales.customers as c inner join sales.transactions as t on c.customer_code=t.customer_code  group by c.customer_type; 

/*Based on region wise sales data , begaluru has lowest sales hence to analyse why bengaluru has lowest sales the below analysis query was done on the distinct count of products sold in each region*/
/*region wise distinct product count*/
Select m.markets_name,count(distinct(product_code)) as "Dsitinct Products" from sales.transactions as t inner join sales.markets as m on m.markets_code=t.market_code group by m.markets_code order by count(distinct(product_code)) ;
