use ai_snega;
delimiter &&
drop procedure if exists singleupdate;&&
create procedure singleupdate
 (
in tablename varchar(100),
in columname varchar(20),
in valuechange varchar(100),
in idname varchar(10),
in idparam int)
begin 
set @statement= concat('update ',tablename,' set ',columnname,' =\'',valuechange,'\'',' where ',idname,'=',idparam);
prepare stmt from @statement;
execute stmt ;
end &&
 
delimiter ;
call singleupdate('ai_snegadurga','email','punitha@gmail.com','sno',13);
select * from ai_snegadurga;
