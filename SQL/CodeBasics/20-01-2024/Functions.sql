delimiter $$
Create Function SimpleFunc( m int)
returns char(4)
Deterministic
begin
 if m<0 then
     return "less"; 
 else
     return "good";
 end if;    
end$$

delimiter ;


Select SimpleFunc(-4);

drop function SimpleFunc;

/* Switch Case Function */

delimiter $$
create function Case1(m int)
returns char(4)
deterministic
BEGIN
  Case m
    when -1 then return "nega";
    when  0 then return  "zero";
    when 1 then return  "posi";
    else
      begin
      end;
  END case;
end$$

delimiter ;

Select case1(+1);

drop function case1;


delimiter $$
create function Case2(m int)
returns char(4)
deterministic
BEGIN
  Case 
    when m<0 then 
            return "nega";
    when  m=0 then return  "zero";
    when m>0 then return  "posi";
  END case;
end$$

delimiter ;

Select case2(-1);

drop function case2;


/*loop function*/

delimiter $$

create function loop1()
returns int
deterministic
begin
   set m=0;
   select 
   
delimiter ;   