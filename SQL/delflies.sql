create trigger update_mile
on flies after insert, delete, update
as
begin
	update passenger set miles = miles + increase from
	(select inserted.passenger_id, sum(distance) as increase from inserted, flight
	 where inserted.flight_code=flight.flight_code group by passenger_id) as insdis
	where passenger.passenger_id=insdis.passenger_id

	update passenger set miles = miles - decrease from
    (select deleted.passenger_id, sum(distance) as decrease from deleted, flight
	 where deleted.flight_code=flight.flight_code group by passenger_id) as deldis
	where passenger.passenger_id=deldis.passenger_id
end