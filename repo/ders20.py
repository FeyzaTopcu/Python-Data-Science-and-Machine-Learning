#for i in range(10):
#    print(i)
#
#number = [x for x in range(10)]
#print(number)
#
#sayi = [x**2 for x in range(10) ]
#
#print(sayi)
#
#
#gezer = [r*r if r%2== 0 else 'TEK' for r in range(10)]
#print(gezer)
#
#kelime = 'Feyza Topçu'
#
#liste = []
#
#for kelimme in kelime:
#    liste.append(kelimme)
#
#print(liste)
#
#
#tarihler = [1989,1961,1959,1997,1992]
#
#ages = [2020 - t for t in tarihler]
#
#print(ages)
#
#artı = [2019 - r for r in tarihler]
#print(artı)
#
#
#result = []
#for x in range(0,3):
#    for y in range(0,3):
#        result.append((x,y))
#    
#print(result)
#
#bilgi = [(x,y) for x in range(3) for y in range(3)]
#print(bilgi)
#
#for c in range(20):
#    if c == 10:
#        break
#    print(c)
#
#for g in range(10):
#    if g == 5:
#        continue
#    print(g)

#f = 0
#while f < 10 :
#    f+=1
#    if f == 2:
#        continue
#    print(f)


toplam = 0
result = 0

while result <= 100:
    result += 1
    if(result % 2 == 1):
        continue
    toplam += result

print(toplam)


for h in range(0,100):

    if h % 2 == 1:   
        continue
    toplam += h
    
print(toplam)    


for item in range(4,255,10):
    print(item)

print(list(range(5,150,10)))

#enumerate 

greeting = 'hebele'

index = 0
for letter in greeting:
    print(f' {index}. index {letter} ')
    index += 1

for letter in enumerate(greeting):
    print(letter)
    index += 1

#zip

list1 = ['dfd','hhjj','wethdf']
list2 = [78,87,98]

print(list(zip(list1,list2)))

for item in zip(list1,list2):
    print(item)
