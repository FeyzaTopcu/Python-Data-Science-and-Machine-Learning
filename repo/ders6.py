names = ['feyza', 'topçu','zeynep','emin', 'reyhan','deniz']
years = [1997,1992,1992,1989,1958,1961]

names.append('cenk')

print(names)

names.insert(0,'sena')

print(names)

names.remove('deniz')
print(names)

j= 'ali' in names
print(j)

names.reverse()

print(names)

names[::-1]


print(names)

years.sort()
print(years)

names[-1:] = [ 'hakan']
print(names)

str = "chevvrolet, Dacia"
ressult = str.split('*')
print(ressult)

r= max(years)
print(r)

t=min(years)
print(t)

i=years.count(1992)

print(i)

ressult.clear()
print(ressult)

lale= []
for l in range (3):
    l=input('marka bilgisi giriniz')
    lale.append(l)
    print(lale)

    fruits = {'banana','apple','cherry'}
    print(fruits)
    
    fruits.add('strawberry')
    fruits.update(['orange','grape'])
    print(fruits)
    fruits.discard("strawberry")
    print(fruits)

    fruits.remove('orange')
    print(fruits)
    fruits.pop()
    print(fruits)