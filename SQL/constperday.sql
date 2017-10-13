alter table flight_instance
add constraint checkperday
check (dbo.checkdeparts()=1)