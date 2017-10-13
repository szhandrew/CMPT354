import pymssql #import python ms sql library
conn = pymssql.connect(host='cypress.csil.sfu.ca',
user='s_zhaohuis', password='7AP62Rbra36MNy7H',
database='zhaohuis354')

mycursor = conn.cursor()

##Test
##s = "YYZ"
##
##mycursor.execute("INSERT INTO Airport(iata, airport_name, city) VALUES('"+s+"','Pearson Intl ','Toronto')")
##
##mycursor.execute('SELECT * from Airport')
##
##row = mycursor.fetchone()
##while row:
##    print "Airport: iata = %s, aname = %s, city = %s" %(row[0], row[1], row[2])
##    row = mycursor.fetchone()

##Add Flies record

import datetime
import time
from datetime import timedelta

fc = raw_input("Enter a flight code: ")
dp = raw_input('Enter departure date with format yyyy-mm-dd ')
date = time.strptime(dp, "%Y-%m-%d")
y,m,d = date[0:3]
dp = datetime.date(y,m,d)
p_id = raw_input("Enter passenger ID: ")

##fc = "JA260"
##p_id = "55146"
##dp = datetime.datetime(2016,12,01)
while True:
    try:
        mycursor.execute("INSERT INTO Flies(flight_code, departs, passenger_id) VALUES(%s, %s, %s)",(fc, dp, p_id))
        break
    except ValueError:
        print("Invalid input!!")

mycursor.execute('SELECT * from Flies')
row = mycursor.fetchone()
while row:
    print "Flies: flight_code = %s, departs = %s, passenger_id = %s" %(row[0], row[1], row[2])
    row = mycursor.fetchone()

##mycursor.close()

##View Passenger Info

mycursor.execute('SELECT * from Passenger')
row = mycursor.fetchone()
for row in mycursor:
    if row[0]==p_id:
        print "Passenger_id = %d, first_name = %s, last_name = %s, miles = %d" %(row[0], row[1], row[2], row[3])
                 



