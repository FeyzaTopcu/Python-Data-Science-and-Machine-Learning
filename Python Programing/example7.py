sayi = int(input("sayi gir"))
tur = True
if sayi == 1 :
    print("1 asal değil")

for i in range(2,sayi):
    if sayi % i == 0:
         tur = False
         break
    else:
        tur = True
        break


if tur == True :
    print("Asal")
else:
    print("Asal değil ")