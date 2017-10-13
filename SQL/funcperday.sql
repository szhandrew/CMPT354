create function checkdeparts()
returns int
as
begin
	declare @result int
	if(exists (select * from flight_instance fi1, flight_instance fi2
				  where fi1.departs=fi2.departs and fi1.flight_code<>fi2.flight_code
				  and fi1.aircraft_id=fi2.aircraft_id))
		set @result = 0
	else
		set @result = 1
	return @result
end