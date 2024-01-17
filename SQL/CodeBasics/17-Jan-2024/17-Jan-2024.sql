SELECT 
    *
FROM
    sales.transactions
LIMIT 5;

sELECT DISTINCT(currency) from sales.transactions;

Select Year(order_date),Sum(t.sales_amount) as "Total Sales" from sales.transactions 
as t where currency in ('INR\r','USD\r') group by year(order_date);

Select Year(order_date),Sum(t.sales_amount) as "Total Sales" from sales.transactions as t group by year(order_date);
/*
2017	93569152   
2018	414308941
2019	336452114
2020	142235559
*/

Select Year(order_date),Sum(t.sales_amount) as "Total Sales" from sales.transactions 
as t where currency in ('INR\r','USD\r') group by year(order_date);

/*
2017	92882653
2018	413687162
2019	336019102
2020	142224545
*/