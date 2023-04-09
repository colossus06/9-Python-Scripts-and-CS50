import datetime


d=datetime.date.today

year, month, day = input("Enter a date: ").split("-")



tdelt= datetime.timedelta(int(year), int(month), int(day))

bday= tdelt - d

print(bday)