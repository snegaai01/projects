use ai_snega;
show databases;
delimiter &&
drop procedure if exists singledelete;&&
delimiter &&
create procedure singledelete
 (
in tablename varchar(100),
in columnname varchar(10))

begin 
set @statement= concat('alter table ',tablename,' drop column ',columnname);
prepare stmt from @statement;
execute stmt ;
end &&
 
delimiter ;
call singledelete('ai_snegadurga','gender');
select * from ai_snegadurga;
