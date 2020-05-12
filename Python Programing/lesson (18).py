sayilar = [1,3,5,7,9,12,19,21]

for i in sayilar:
    if i %3 == 0:
        print(i)

    else:
        pass 
print("*" *50)
toplam = 0

for sayi in sayilar:
    toplam += sayi
        
print("toplam :", toplam)

print("*" *50)
kare = 1
for k in sayilar:
    if k %2 != 0:
        kare = k*k
        print(f'{k} nın karesi {kare}')
print(f'tek sayıların karesi  {kare}')

print("*"*50)

sehirler = ["kocaeli","istanbul","ankara","izmir","rize","muş"]

for karekter in sehirler:
    if len(karekter) > 5:
        print(karekter)
    else:
        pass

print("*"*50)

urunler = [

    { 'name' : 'Samsung S6', 'price' : '3000'},
    {'name' : 'Samsung S7', 'price' : '4000'},
    { 'name' : 'Samsung S8', 'price' : '5000'},
    {'name' : 'Samsung S9', 'price' : '6000'},
    {'name' : 'Samsung S10', 'price' : '7000'}
]
fiyat = 0
for urun in urunler:
    fiyat += int(urun['price'])

print(fiyat)
print('*'*50)

for y in urunler:
    if int(y['price']) > 5000:
        print(y)
