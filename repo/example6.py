sayilar = [ 1,3,5,7,9,12,19,21]
uzunluk = len(sayilar)
print("*"*2)
p=0
while p < len(sayilar):
   print(sayilar[p])
   p += 1
print("*"*2)

for i in range(len(sayilar)):
   print(sayilar[i])
print("*"*2)
t = 0
while t < len(sayilar):
   print(sayilar[t])
   t += 1    
   
baslangic = int(input("Başlangıç değeri "))
bitis = int(input("bitiş değeri "))

sayii = baslangic 
while sayii <= bitis:
   print(sayii)
   sayii += 1

print("**"*15)

r = 100
while r>0:
   print(r)
   r -= 1

   

print("**"*15)

sayiDizisi = []
for y in range(0,5):
   b=int(input("Rakam:"))
   sayiDizisi.append(b)


sayiDizisi.sort()
print(sayiDizisi)

print("**"*15)

urunler = []

adet = int(input("Ürün sayısı:"))

i = 0

while(i < adet):
    name = input('Ürün ismi')
    price = input('Ürün fiyatı')

    urunler.append({
        'name'  : name,
        'price' : price
    })
    i += 1


for urun in urunler:
    print(f' ürün adı {urun["name"]} fiyatı {urun["price"]}')

