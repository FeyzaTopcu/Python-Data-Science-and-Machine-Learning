cities= {'iz','ge','le','me'}
print(cities)

cities.add('nasi')
print(cities)

cities.update(['fe','na'])
print(cities)

cities.remove('iz')
print(cities)

cities.discard('fee')
print(cities)

cities.clear()
print(cities)

del cities

cities= {'iz','ge','le','me'}
print(cities)

cities.add('nasi')
print(cities)

cities.update(['fe','na'])
print(cities)


de= ('fe','za','hanim','fse','zsa','hansim','za','hanim')
print(de[2:])
print(de[-2:])
print(de[:-2])
print(de[:])

print('fe' in de)
print('fdfde' in de)

tr= tuple(set(de))

tre= list(de)