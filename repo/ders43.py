from datetime import datetime
from datetime import timedelta
result = dir(datetime)

print(result)


result= datetime.now()


print(result)

simdi = datetime.now()

result = simdi.year

print(result)

result= simdi.month


print(result)

result = simdi.day


print(result)

result = simdi.hour

print(result)

result = simdi.minute

print(result)

result = simdi.second

print(result)

result = datetime.ctime(simdi)

print(result)

result = datetime.strftime(simdi,'%Y')

print(result)

result = datetime.strftime(simdi,'%X')

print(result)

result = datetime.strftime(simdi,'%d')


print(result)

result = datetime.strftime(simdi,'%A')

print(result)

result = datetime.strftime(simdi,'%B')

print(result)

result = datetime.strftime(simdi,' %Y %B %A')

print(result)


str_date = '04 August 2019 hour 11:11:11'
print('Value of str_date is:', str_date)
print('Type of str_date is:', type(str_date))

print('+++++++++++++ After using strptime() method++++++++++++')
date_obj = datetime.strptime(str_date, "%d %B %Y hour %H:%M:%S")
print('Value of date_obj is:',date_obj)
print('Type of date_obj is:',type(date_obj))

birthday = datetime(1997,11,3,9,30,10)
result = datetime.timestamp(birthday) #saniye
result = datetime.fromtimestamp(result) #saniye to datetime
result = datetime.fromtimestamp(0)
print(result)

result = simdi - birthday
print(result)

#result = result.days

#result = result.seconds

#result = result.microseconds

#result = simdi + timedelta(days=10)

result= simdi +timedelta(days=765, minutes=410)

result = simdi -timedelta(days= 409, minutes=1002 ) 
print(result)

