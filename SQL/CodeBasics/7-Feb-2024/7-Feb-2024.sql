Select sum(NormalizedSalesAmount) as "Total Sales" from cleanedtransactions where market_code="Mark001" and Year(order_date)=2020 limit 5;

Select * from markets;

Select * from cleanedtransactions limit 5;

Select sum(NormalizedSalesAmount) as "Total Sales",custmer_name from cleanedtransactions as t inner join customers as c on t.customer_code=c.customer_code group by custmer_name order by sum(NormalizedSalesAmount) desc;

Select * from date;