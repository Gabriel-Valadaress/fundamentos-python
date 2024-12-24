#Transform a number of minutes (input) in hours and minutes
#Example: 150 minutes is 2 hours and 30 minutes

minutes = float(input("Type a number of minutes: "))

hours = int(minutes // 60)
leftMinutes = int(minutes % 60)
print("%d minutes equals to %d hours and %d minutes." %(minutes, hours, leftMinutes))
