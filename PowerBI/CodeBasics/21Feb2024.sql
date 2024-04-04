Select * from date limit 5;

Alter table date add MonthNumber int ;

update date set MonthNumber=month(date);

Select * from cleanedtransactions limit 5;

Select sum(NormalizedSalesAmount),product_code from cleanedtransactions group by product_code order by sum(NormalizedSalesAmount) desc;

Select count(distinct(product_code)) from cleanedtransactions;

Select sum(NormalizedSalesAmount),c.custmer_name from cleanedtransactions as t inner join customers as c on t.customer_code=c.customer_code  group by c.customer_code order by sum(NormalizedSalesAmount) desc;


Select * from cleanedtransactions where ProfitMargin is null;

Alter table cleanedtransactions add ManualProfitMarginPercentage double default null;

Select 4/2;

Update cleanedtransactions set ManualProfitMarginPercentage= (ProfitMargin/sum(ProfitMargin));

Select * from cleanedtransactions limit 5;


Select sum(ProfitMarginPercentage),m.markets_name from cleanedtransactions as ct inner join markets as m on m.markets_code=ct.market_code group by m.markets_name order by sum(ProfitMarginPercentage) desc;


Select sum(ProfitMargin) from cleanedtransactions;

/*
'24657068.409999933'
*/

Select sum(NormalizedSalesAmount) from cleanedtransactions;

/*
'984872713'
*/

Select distinct(customer_type) from customers limit 5;

/**/
