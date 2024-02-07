delimiter &&
drop procedure if exists ai_snegadurga;&&
create procedure ai_snegadurga
(
in snoparam int,

in emailparam varchar(50)
)
begin 
 insert into ai_snegadurga(sno,email)values(snoparam,emailparam);
 end &&
 delimiter ;
 call ai_snegadurga('13','punitha@gmail');