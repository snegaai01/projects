use ai_snega;
delimiter &&
drop procedure if exists singledelete;&&
delimiter &&
create procedure singledelete
 (
in tablename varchar(100),
in columnname varchar(10))

begin 
set @statement= concat('alter table ',tablename,' add column ',columnname,' varchar \(50\)');
prepare stmt from @statement;
execute stmt ;
end &&
 
delimiter ;
call singledelete('ai_snegadurga','email');

select * from ai_snegadurga;
