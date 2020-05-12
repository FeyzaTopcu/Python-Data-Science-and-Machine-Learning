list = [1,2,3]
tuple = (1,2,'üç','feyza','feyza')

print(type(list))
print(type(tuple))

print(len(tuple))
print(len(list))

print(list[1])
print(tuple[1])

print(tuple.count('feyza'))
print(tuple.index('feyza'))
 
de = ('hatice', 'derya') + tuple
print(de)

plakalar = { 'ankara': '06', 'istanbul': '34', 'manisa' : '45'}

print(plakalar)
plakalar['zonguldak'] = 67

print(plakalar)

plakalar['ankara'] = 'new value'
print(plakalar) 


users = {
 'sadık turan' : 2,
'çınar turan' : 3,
'hafza turan' : {'age': 41, 'mail': 'www.google.com.tr', 'mahalle': [34,56]}

}

print(users['hafza turan']['mail'])