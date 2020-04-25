#isim = str(input("isim : "))
#egitim = str(input("Eğitim durumu :"))
#yas = int(input("Yaş:"))
#
#if (yas > 18) and ((egitim == "lise") or (egitim == "üniversite")) :
#    print("Ehliyet alabilirsiniz")
#else :
#    print("Ehliyet alamazsınız")
#
#print("**"*20)
#


#09toplam = 0
#for i in range(2):
#    yazili = int(input("Yazili notunu giriniz:" ))
#    toplam += yazili
#   
#
#sozlu = int(input("Sözlü notunu giriniz:"))
#
#ortalama = (toplam + sozlu)/3
#
#if  0 < ortalama < 24:
#   print(f"Ortalamanız {ortalama} Ders notunuz 0")
#elif 24 < ortalama < 44:
#   print(f"Ortalamanız {ortalama} Ders notunuz 1")
#elif 44 < ortalama < 54:
#   print(f"Ortalamanız {ortalama} Ders notunuz 2")
#if  54 < ortalama < 69:
#   print(f"Ortalamanız {ortalama} Ders notunuz 3")
#elif 69 < ortalama < 84:
#    print(f"Ortalamanız {ortalama} Ders notunuz 4")
#elif 84 < ortalama < 100:
#    print(f"Ortalamanız {ortalama} Ders notunuz 5")

import datetime

trafik_cikis_tarihi =input("Trafiğe çıkış tarihini yazınız (yy/aa/gg)")
trafik_cikis_tarihi = trafik_cikis_tarihi.split('/')
trafik_cikis_tarihi = datetime.datetime(int(trafik_cikis_tarihi[0]),int(trafik_cikis_tarihi[1]),int(trafik_cikis_tarihi[2]))
simdi = datetime.datetime.now()
fark = simdi - trafik_cikis_tarihi
gun = fark.days
print(fark)

if gun <= 365:
    print("1.Servis aralığı")
elif gun <= 365 and gun <=365*2:
    print("2.Servis aralığı")
elif gun <= 365*2 and gun <=365*3:
    print("3.Servis aralığı")

else:
    print("Hatalı giriş")