x = 0

while x < 100 :
    print(x)
    x = x+1

print(x)

print("*"*50)
x = 1
while x<100:
    if x %2 == 0:
        print(f' {x} sayısı çifttir')
    else:
        print(f'{x} sayısı tektir')
    x += 1

print('bitti ...')

print("*" *50)

isim= '' # false
while not isim.strip():
    isim = input('isminizi giriniz')

print(f'Merhaba {isim}')


kelime = 'Feyza Topçu'

for r in kelime:
    if r == 'a':
        break
    
    print(r)

for zaa in kelime:
    if zaa == 'z':
        continue
    print(zaa) 
print("*"*50)
result =0
he =1
while he <= 100:
    he +=1
    if he % 2 == 1:
        continue
    result += he
print(f'toplam : {result}')
print("**"*20)
for item in range(5,100,20):
    print(item)
    
print(list(range(5,35,2)))

#enumerate

index = 0
greeting = "hello guys"

for letter in greeting:
    print(f'index : {index} letter : {greeting[index]}')
    index +=1


for indexx,kelimee in enumerate(greeting):
    print(f' index : {indexx} letter : {kelimee}')

#eşleştirme metodu - zip metodu 

list1 = [5,8,9,6,3]
list2 = ['f','e','y','z','a']
list3 = [100,200,300,400,500]
print(list(zip(list1, list2,list3)))


for k,l,m in zip(list1,list2,list3):
    print(k,l,m)


 