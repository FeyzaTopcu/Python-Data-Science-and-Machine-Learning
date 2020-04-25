import random
sayi = int(input("1 ile100 arasında sayı gir :"))
deger = random.randint(1,100)
print(deger)
hak = 1
while (deger != sayi )  :
    if hak < 5:
        if sayi < deger :
            print("Daha büyük sayı giriniz")
            sayi = int(input("1 ile100 arasında sayı gir :"))
        elif sayi > deger:
            print("Daha küçük sayı giriniz")
            sayi = int(input("1 ile100 arasında sayı gir :"))
        else  :
            print("Sayıyı buldunuz")   
        hak += 1
    else:
        print("Hakkınız bitti")
        break