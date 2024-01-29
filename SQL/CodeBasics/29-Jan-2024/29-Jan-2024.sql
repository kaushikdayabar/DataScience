/*Normalizing Sales Amount in different currencies using Update Command*/
update cleanedtransactions set NormalizedSalesAmount=80*sales_amount where currency='USD\r';

Alter table cleanedtransactions modify column NormalizedSalesAmount bigint(255);

Select * from cleanedtransactions limit 5;

Select * from date limit 5;

Select sum(NormalizedSalesAmount),Sum(sales_qty) from cleanedtransactions;


