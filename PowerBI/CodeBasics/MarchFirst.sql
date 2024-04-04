-- 29 March 2024

Select * from cleanedtransactions limit 5;
/*
Prod001	Cus001	Mark001	2017-10-10	100	41241	INR 41241	1			
Prod002	Cus003	Mark003	2018-04-06	1	875	INR 875	2			
Prod002	Cus003	Mark003	2018-04-11	1	583	INR 583	3			
Prod002	Cus004	Mark003	2018-06-18	6	7176	INR 7176	4			
Prod003	Cus005	Mark004	2017-11-20	59	500	USD 40000	5			
    */
    
Select * from dump2 limit 5;

/*
Prod279	Cus020	Mark011	2020-01-08	1	102	INR	0.34	34.68	67.32	1
Prod279	Cus020	Mark011	2020-01-09	1	102	INR	-0.16	-16.32	118.32	2
Prod279	Cus020	Mark011	2020-01-10	1	102	INR	0.02	2.04	99.96	3
Prod279	Cus020	Mark011	2020-01-20	1	102	INR	-0.1	-10.2	112.2	4
Prod281	Cus020	Mark011	2018-08-22	1	102	INR	-0.09	-9.18	111.18	5
										*/
                                        
                                        
Update cleanedtransactions set 
ProfitMargin=(Select ProfitMargin from dump2 where dump2.IDUnique=cleanedtransactions.IDUnique),
CostPrice=(Select CostPrice from dump2 where dump2.IDUnique=cleanedtransactions.IDUnique);

Select * from cleanedtransactions where ProfitMarginPercentage is null;                                        