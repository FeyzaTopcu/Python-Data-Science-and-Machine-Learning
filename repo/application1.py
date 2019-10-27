my= "selam\'s canim"
print(my)

message= 'merhaba {} '
print(message.format(my))

name= "feyza ben memnun oldum"

print(name.title())
print(name.lower())

print(name.count('m'))
print(name.find('n'))
print(name.replace('oldum','hissediyorum'))
print(dir(name))
print(help(str))

age=21
mms= "ben " + str(age) + " yasindayim"
print(mms)

s="hey"

print(s*4)
cities= ['barcelona','ispanya','almanya','ingiltere']

cities[0]='turkiye'
print(cities)

cities.append('somali')
print(cities)

cities.insert(0,'izmir')
print(cities)

del(cities[4])
print(cities)

cities= ['barcelona','ispanya','almanya','ingiltere']
cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)


print(sorted(cities))
print(cities)
