import datetime
from datetime import date
from datetime import time


timeNow = datetime.datetime.now()
timeBirthday = datetime.datetime(2021, 10, 15)
birthday = timeNow - timeBirthday

if int(birthday.days) == 0:
    print("Hari ini",timeNow.day, timeNow.strftime("%A - %b - %Y") ,"adalah hari lahir anda, selamat ulang tahun")
elif int(birthday.days) < 0 :
    print("hari lahir anda ", birthday.days, " Hari")
else :
    print("hari lahir anda sudah lewat", birthday.days, " Hari")
    
    
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)


waktu = time(2,30,22)
print(waktu)

print("-"*100)

from datetime import datetime

dateAsString = '15 October, 2021'
date = datetime.strptime(dateAsString, "%d %B, %Y")
print(date)
