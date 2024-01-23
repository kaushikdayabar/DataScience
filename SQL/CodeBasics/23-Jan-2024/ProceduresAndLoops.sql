DROP PROCEDURE PROC1;

Delimiter $$
create procedure proc1()
begin
set @p1=0;
repeat
 set @p1=@p1+1;
until @p1=5 end repeat;
Select @p1;
end $$
Delimiter ;


call proc1();


