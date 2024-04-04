Select sum(ProfitMargin),market_code from cleanedtransactions group by market_code order by sum(ProfitMargin) asc;

-- Profit Margin Validation Completed and All Good
Select sum(ProfitMargin),markets_name from cleanedtransactions as ct inner join markets as m on m.markets_code=ct.market_code group by market_code order by sum(ProfitMargin) desc;

Select * from cleanedtransactions limit 5;

-- Profit Margin Percentage Completed and All Good
Select sum(ProfitMargin)/sum(NormalizedSalesAmount)*100,markets_name from cleanedtransactions as ct inner join markets as m on m.markets_code=ct.market_code group by market_code order by sum(ProfitMargin)/sum(NormalizedSalesAmount) desc;

-- Revenue Contribution Percentage Completed and All Good
Select (sum(NormalizedSalesAmount)/(Select sum(NormalizedSalesAmount) from cleanedtransactions))*100 ,m.markets_name
from cleanedtransactions as ct inner join markets as m on m.markets_code=ct.market_code
group by m.markets_name
order by sum(NormalizedSalesAmount)/(Select sum(NormalizedSalesAmount) from cleanedtransactions) desc;

-- Tabular Visualization

   -- Revenue Column
   Select sum(NormalizedSalesAmount),c.custmer_name from cleanedtransactions as ct inner join customers as c on c.customer_code=ct.customer_code group by c.customer_code order by sum(NormalizedSalesAmount) desc ;
   
   -- Revenue Contribution Percentage,TotalProftiMargin%,TotalProfitMarginContribution% (USED BELOW QUERY ITSELF WITH MINOR MODIFICATIONS)
   Select 100*sum(ProfitMargin)/(Select sum(ProfitMargin) from cleanedtransactions),c.custmer_name from cleanedtransactions as ct inner join customers as c on c.customer_code=ct.customer_code group by c.customer_code order by sum(NormalizedSalesAmount) desc ;
   
-- Revenue Trend

Select * from cleanedtransactions limit 5;

-- Revenue Trend verified and all good
Select sum(NormalizedSalesAmount),monthname(order_date),year(order_date) 
from cleanedtransactions 
group by monthname(order_date),year(order_date)
order by monthname(order_date) asc;

-- Sum Profit Margin

Select 100*sum(ProfitMargin)/Sum(NormalizedSalesAmount),monthname(order_Date) from cleanedtransactions where Year(order_Date)=2020 group by monthname(order_Date);

-- Profit Margin Percentage Distribution across zones drilled down to states

Select m.zone,m.markets_name,100*sum(ProfitMargin)/sum(NormalizedSalesAmount) from cleanedtransactions as ct inner join markets as m on m.markets_code=ct.market_code group by m.zone,m.markets_name order by m.zone desc,m.markets_name desc;

Select * from markets;