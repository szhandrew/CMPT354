alter table flight
add constraint diffdeparr
check(dbo.checkdiff()=1)