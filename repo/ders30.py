import random 

#result = dir(random)


#result = help(random)
#print(result)

#result = random.random() * 100
#result = int(random.uniform(10,100))

#result = random.randint(1,100)

names = ['emin','zeynep','şüheda','reyhan','feyza']
result = names[random.randint(0,len(names)-1)]
print(result)
sehir = ['ankara','istanbul']
result = sehir[random.randint(0,len(sehir)-1)]
print(result)

result = random.choice(names)
print(result)

yazi = 'selam naber'

result = random.choice(yazi)
print(result) 


liste = list(range(10))
print(liste)

random.shuffle(liste)

result = liste

print(result)

liste = range(100)

result = random.sample(liste,3)
print(result)

result= random.sample(names,2)
print(result)

