#dates
import datetime

x = datetime.datetime.now()
print(x) # The date contains year, month, day, hour, minute, second, and microsecond.
print(x.year)
print(x.month)
print(x.strftime("%B"))
print(x.day)
print(x.strftime("%A")) #The week day
