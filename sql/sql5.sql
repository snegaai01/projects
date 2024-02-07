use ai_snega;
delimiter &&
drop procedure if exists singledelete;&&
create procedure singledelete
 (
in tablename varchar(100),
in idname varchar(10),
in idparam int)
begin 
set @statement= concat('delete ','from ',tablename,' where ',idname,'=',idparam);
prepare stmt from @statement;
execute stmt ;
end &&
 
delimiter ;
call singledelete('ai_snegadurga','sno',11);
select * from ai_snegadurga;
