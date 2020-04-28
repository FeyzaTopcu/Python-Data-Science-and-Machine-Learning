numbers = []

for x in range(10):
    numbers.append(x)
print(numbers)

numbers = [ x for x in range(10)]
print(numbers)

melek = [y for y in  range(15)]
print(melek)

kaktus = [z for z in range(20)]
print(kaktus)

for x in range(15):
    print(x **2)

numbers = [x**3 for x in range(10) ]
print(numbers)

makale = [x*x for x in range(10) if x %3 == 0 ]

yit = [v**5 for v in range(5) ]
print(yit)


myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

yu = [letter for letter in myString]
print(yu)


years = [1959,1961,1989,1992,1997]
ages = [2020 - year for year in years]
print(ages)

results = [x if x %2 ==0 else 'TEK' for x in range(1,10)]
print(results)

yakap= [g if g %3 ==0 else 'Üçe bölünmez' for g in range(1,10)]
print(yakap)

re = []
for t  in range(3):
    for h in range(5):
       re.append((t,h))

print(re)      


tec = [(x,y) for x in range(5) for y in range(2)]
print(tec)

