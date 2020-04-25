sayilar= [1,3,5,7,9,12,19,21]

i=0
while i < len(sayilar):
    print(sayilar[i])
    i+=1


print("*"*50)

baslangic = int(input("baslangıc rakamı giriniz"))
bitis =int(input("bitis rakamı giriniz"))

l = baslangic

while l < bitis:
    l += 1
    print(l)

print("*"*50)

k =100
while k>=0:
    print(k)
    k-= 1
print("*"*50)

y = []
#for o in range (5):
#    po = int(input("bir rakam giriniz"))
#    y.append(po)


y.sort()
print(y)

print("*"*50)

urunlistesi = {}
urunsayisi = int(input("Kaç ürün gireceksiniz"))
t=0
while t <= urunsayisi:
     urunismi= input("Ürününüzün adını giriniz")
     urunfiyat =int(input("ürünün fiyatı nedir"))
     urunnumarası =int(input("ürünün numarası nedir"))
     urunlistesi.update(
         {
             urunnumarası:{

                 'isim': urunismi,
                 'fiyat' : urunfiyat
             }
         })
     t += 1
     print(urunlistesi)



