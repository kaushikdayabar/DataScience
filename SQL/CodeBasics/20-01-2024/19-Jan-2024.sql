
Select * from transactions where currency='INR\r' limit 5;

/*
'Prod001', 'Cus001', 'Mark001', '2017-10-10', '100', '41241', 'INR\r', NULL
'Prod001', 'Cus002', 'Mark002', '2018-05-08', '3', '-1', 'INR\r', NULL
'Prod002', 'Cus003', 'Mark003', '2018-04-06', '1', '875', 'INR\r', NULL
'Prod002', 'Cus003', 'Mark003', '2018-04-11', '1', '583', 'INR\r', NULL
'Prod002', 'Cus004', 'Mark003', '2018-06-18', '6', '7176', 'INR\r', NULL
*/
Select * from transactions where currency='INR' limit 5;
/*
'Prod001', 'Cus001', 'Mark001', '2017-10-10', '100', '41241', 'INR', NULL
'Prod001', 'Cus002', 'Mark002', '2018-05-08', '3', '-1', 'INR', NULL
'Prod002', 'Cus003', 'Mark003', '2018-04-06', '1', '875', 'INR', NULL
'Prod002', 'Cus003', 'Mark003', '2018-04-11', '1', '583', 'INR', NULL
'Prod002', 'Cus004', 'Mark003', '2018-06-18', '6', '7176', 'INR', NULL
*/

/*Conclusion:
The rows are equal hence it must be duplicate only proceeding with their removal
*/

Select count(*),Currency from transactions group by currency;

/*
'279', 'INR'
'2', 'USD'
'150000', 'INR\r'
'2', 'USD\r'
*/

/*creating new table with filtered currency values to avoid messing with original data*/
create table CleanedTransactions as select * from transactions where currency in ('INR\r','USD\r');


Select distinct(currency) from cleanedtransactions;
/*
'INR\r'
'USD\r'
*/

Select count(*) from cleanedtransactions where sales_amount<=0;
/*
'1607'
*/

/*deleting meaning less data: where there is a transaction sales amount can never be zero*/
delete from cleanedtransactions where sales_amount<=0;

Select count(*) from cleanedtransactions where sales_amount<=0;
/*
0
*/
