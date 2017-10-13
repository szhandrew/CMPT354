create trigger del_pas
on Passenger for delete
as
if exists 
(select * from flies, deleted
 where Flies.passenger_id=deleted.passenger_id)
begin
	declare @num int
	set @num = (select count(*) from flies, deleted
			    where Flies.passenger_id=deleted.passenger_id)
	raiserror(@num,16,1)
end