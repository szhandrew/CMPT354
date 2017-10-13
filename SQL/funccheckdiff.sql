create function checkdiff()
returns int
as
begin
	declare @result int
	if(exists (select * from flight f1, flight f2
				  where f1.flight_code=f2.flight_code
				  and f1.departure_iata=f2.arrival_iata))
		set @result = 0
	else
		set @result = 1
	return @result
end