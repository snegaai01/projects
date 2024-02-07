use ai_snega;
create table ai_snegadurga1(sno int not null primary key ,name varchar(50),gender varchar(10),phone long,pincode long);
show tables;

select * from ai_snegadurga;

delimiter &&
drop procedure if exists ai_snegadurga;&&
create procedure ai_snegadurga
(
in snoparam int,
in nameparam varchar(20),
in genderparam varchar(10),
in phoneparam long,
in pincodeparam long,
in emailparam varchar(50)
)
begin 
 insert into ai_snegadurga(sno,name,gender,phone,pincode,email)values(snoparam,nameparam,genderparam,phoneparam,pincodeparam,emailparam);
 end &&
 delimiter ;
  call ai_snegadurga(13,'punitha','Female',621105,'punitha@gmail.com');
 select * from ai_snegadurga;
 
 
  