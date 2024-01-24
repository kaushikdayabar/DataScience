Select * from cleanedtransactions limit 5;

/* transactions with sales amount less than 1 is removed*/
Select count(*) from cleanedtransactions where sales_amount<=0;

/*Duplicate transactions removed */
Select distinct(currency) from cleanedtransactions;

/*total number of transactions*/
Select count(*) from cleanedtransactions;
/*
# count(*)
'148395'
*/

/* no primary ID column for transactions table*/
Alter table cleanedtransactions add column ID int;	

/*generated unique column */
create table cleanedTransactions1 as Select *,Row_number() over() as IDUnique from cleanedtransactions; 

select * from cleanedtransactions1 limit 5;
/*
product_code, customer_code, market_code, order_date, sales_qty, sales_amount, currency, NormalizedSalesAmount, ID, IDTemp, IDUnique
'Prod001', 'Cus001', 'Mark001', '2017-10-10', '100', '41241', 'INR\r', NULL, NULL, NULL, '1'
'Prod002', 'Cus003', 'Mark003', '2018-04-06', '1', '875', 'INR\r', NULL, NULL, NULL, '2'
'Prod002', 'Cus003', 'Mark003', '2018-04-11', '1', '583', 'INR\r', NULL, NULL, NULL, '3'
'Prod002', 'Cus004', 'Mark003', '2018-06-18', '6', '7176', 'INR\r', NULL, NULL, NULL, '4'
'Prod003', 'Cus005', 'Mark004', '2017-11-20', '59', '500', 'USD\r', NULL, NULL, NULL, '5'

*/

/*deleting useless columns */
alter table cleanedtransactions1 drop ID ,drop IDTemp;

select * from cleanedtransactions1 limit 5;   
/*
# product_code, customer_code, market_code, order_date, sales_qty, sales_amount, currency, NormalizedSalesAmount, IDUnique
'Prod001', 'Cus001', 'Mark001', '2017-10-10', '100', '41241', 'INR\r', NULL, '1'
'Prod002', 'Cus003', 'Mark003', '2018-04-06', '1', '875', 'INR\r', NULL, '2'
'Prod002', 'Cus003', 'Mark003', '2018-04-11', '1', '583', 'INR\r', NULL, '3'
'Prod002', 'Cus004', 'Mark003', '2018-06-18', '6', '7176', 'INR\r', NULL, '4'
'Prod003', 'Cus005', 'Mark004', '2017-11-20', '59', '500', 'USD\r', NULL, '5'

*/
