monster_1= {'name': 'guru', 'power': 10, 'color':'red', 1:'next'}



print(monster_1)
print(monster_1['name'])
print(monster_1['color'])
print(monster_1[1])

print(monster_1)

monster_1['position']=5

print(monster_1)
print(monster_1.get('name'))

print(monster_1.get('nae'))

monster_1['derece'] = 800

print(monster_1)


monster_1.update({'name': 'reyyan', 'power': 84})
print(monster_1)

del monster_1['derece']
print(monster_1)

pops= monster_1.pop('position')

print(pops)
print(len (monster_1))
print(monster_1.keys())
print(monster_1.values())
print(monster_1.items())



monster_1= {'name': 'guru', 'power': 10, 'color':'red', 1:'next'}

for key in monster_1.keys():
    print(key)

    
monster_1= {'name': 'guru', 'power': 10, 'color':'red', 1:'next'}

for key in monster_1.values():
    print(key)

friend = [
        {'adress': 'school', 'empty': 'yes'},

    {'adress': 'home', 'empty': 'no'}
    ]
print(friend[0]['adress'])