1
def goster(kelime,kackez):
   t = 0
   while t < kackez:
       print(kelime)
       t += 1

goster(' tuhaf hayat ',5)

2

def sayilar(*params):
   liste = []
   for i in params:
       liste.append(i)
    print(liste)

sayilar(4,7,5,8,9,6,2,4,120,5,2,30)

3

def asalSayilariBul(baslangic,bitis):
   for sayi in range(baslangic,bitis+1):
       if sayi > 1:
           for l in range(2,sayi):
               if sayi % l == 0:
                   break
           else:
               print(sayi)


baslangic = int(input("başlangıç değeri "))
bitis = int(input("bitiş değeri "))

asalSayilariBul(baslangic,bitis)

def BolenBul(sayi):
    bolenListesi = []
    for i in range(1,sayi):
        if (sayi % i == 0):
            bolenListesi.append(i)
        
    print(bolenListesi)       
        
        
sayi = int(input("sayı  değeri "))

BolenBul(sayi)