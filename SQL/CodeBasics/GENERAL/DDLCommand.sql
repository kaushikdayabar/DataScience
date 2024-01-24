/*add column*/
Alter table cleanedtransactions add column ID int;	

/*deleting useless columns */
alter table cleanedtransactions1 drop ID ,drop IDTemp;


/*-------------------------------Table Operations-----------------------*/
/*deleting table*/
drop table cleanedtransactions;

/*rename table name*/
alter table cleanedtransactions1 rename cleanedTransactions;

/*creating table generated unique column */
create table cleanedTransactions1 as Select *,Row_number() over() as IDUnique from cleanedtransactions; 


/*----------------------------------------------------------General Commands -------------------------------------------*/
/*to see all tables*/
show tables;