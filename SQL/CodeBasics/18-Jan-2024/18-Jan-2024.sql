SELECT 
    SUM(sales_amount)
FROM
    sales.transactions AS t
        INNER JOIN
    sales.date AS dt ON t.order_date = dt.date
WHERE
    dt.date_yy_mmm = '20-Feb\r'
    and 
    currency in ('INR\r','USD\r')
    ;

Select Sum(sales_amount) from sales.transactions where year(order_date)=2020 and Month(order_date)=1;

Select * from sales.date where year=2020 ; 

Select Distinct(currency) from transactions;

Select Max(sales_amount) from sales.transactions;

Alter Table transactions add NormalizedSalesAmount decimal(10,2);
/* 
'INR'
'USD'
'INR\r'
'USD\r'

'2020-01-01', '2020-01-01', '2020', 'January', '20-Jan\r'

*/