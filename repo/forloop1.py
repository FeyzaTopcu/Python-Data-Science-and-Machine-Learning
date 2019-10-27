num1 = int(input('Lutfen bir sayi giriniz'))

if(num1 % 2 == 0): print(f'{num1} cift sayidir')

else:
    print(f'{num1} tek sayidir')


numara= int(input('Lütfen bir değer giriniz: '))

faktoriyel=1
if numara<0:
    print(f'{numara} sayısı negatif bir sayı')
elif numara ==0:
    print(f'{numara} sayısının faktoriyeli : {faktoriyel}')
else:
    for x in range(1,numara+1):
        faktoriyel=faktoriyel*x
print(f'{numara} sayısının faktoriyeli : {faktoriyel}')


friends = ['gaye','lale','cinar','orhan']
for i, friend in enumerate(friends):
    print(i,friend)

palm = ['gaye','lale','cinar','orhan','yagiz']
 
for u,palmm in enumerate(palm):
    print(u,palmm)


case= {'deniz': 15 ,'mert': 85, 'gamze':885,'ymze': 74,'gaye':44}

for key , value in case .items():
    if key == 'mert':
        continue
    print(key,value)



case2= {'lale': 5, 'deniz': 15 ,'mert': 85, 'gamze':88,'ymze': 74,'gaye':44}
for k,v in case2.items():
   
    if k == 'ymze':
        break
    print(k,v)

for o in case2.values():
    print(o)


for x in range(3,15,5):
    print(x)


sayi = [2,5,8,9]

for la in sayi:
    print(la)


notes = {'lale': 5, 'deniz': 15 ,'mert': 85, 'gamze':88,'ymze': 74,'gaye':44}

for p,c in notes.items():
    if c>=60:
        print(f'{p} \'nin aldığı not {c} : GEÇTİ')
    else:
     print(f'{p} \'nin aldığı not {c} : KALDI')