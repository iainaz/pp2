#write a program to subtract five days from current date
import datetime
x=datetime.datetime.now()
y=x-datetime.timedelta(days=5)
print(y)