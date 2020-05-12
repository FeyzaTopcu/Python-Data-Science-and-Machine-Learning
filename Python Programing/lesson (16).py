x = 65
y=55
result = (x > 60 ) and (x < 90)

print(result)

result = (x<5) or (x>60)
print(result)

result= not (x >0)
print(result)

result = x // y
print(result)

numbers = 1,5,8,9
x,*y,z = numbers
result = z** 3 

x=y= [1,2,3]
z = [1,2,3]
print(x is z)
print(x is y)

d = ['banana', 'apple']

k = 'banana' in d
print(k)

name = 'feyza'

print('e' in name)


username = 'feyzatopcu'
password = '123'

if (username == 'feyzatopcu'):
    if(password == '123'):
        print("hoşgeldiniz")
else :
    print("username yada password hatalı")