import datetime
date_import = input()
day, month, year = map(int, date_import.split(','))
date1 = datetime.datetime(day, month, year)
Previous_Date = datetime.date1 - datetime.timedelta(days=1)
print (Previous_Date)