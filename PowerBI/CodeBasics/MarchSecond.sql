Select markets_name,sum(ProfitMargin) from cleanedtransactions as ct inner join markets as m on m.markets_code=ct.market_code group by markets_name order by sum(ProfitMargin) desc;

Select Sum(ProfitMargin) from cleanedtransactions where market_code='Mark008';

Select * from markets where markets_code='Mark008';

Select IDUnique from cleanedtransactions where market_code='Mark008';