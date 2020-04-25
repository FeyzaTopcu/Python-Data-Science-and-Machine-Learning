#sayi = float(input("0 ile 100 arasında sayı giriniz "))
#
#if (sayi > 0) and (sayi <= 100):
#    print(f' {sayi} 1 ile 100 arasındadır')
#else:
#    print(f'{sayi} 1 ile 100 arasında değildir')


#poz_cift = int(input("Pozitif çift sayı giriniz"))
#
#if (poz_cift > 0) and (poz_cift % 2 ==0 ):
#    print(f'{poz_cift} çift ve pozitiftir')
#elif (poz_cift > 0) and (poz_cift % 2 == 1): 
#    print(f'{poz_cift} tek ve pozitif') 
#elif (poz_cift < 0) and (poz_cift % 2 == 0):
#   print(f'{poz_cift} çift ve negatiftir')
#elif (poz_cift < 0) and (poz_cift % 2 == 1):
#   print(f'{poz_cift} tek ve negatiftir')

#email = "feyzatopcu@gmail.com"
#password = "abc"
#
#mailAl = str(input("Mail adresi giriniz"))
#PaswAl = str(input("Şifreyi giriniz "))
#
#if (mailAl == "feyzatopcu@gmail.com") and (password == "abc"):
#    print("Uygulamaya giriş başarılı")
#else:
#    print("Giriş başarısız")



#a = int(input("Sayı gir"))
#b = int(input("Sayı gir"))
#c = int(input("Sayı gir"))
#
#if (a>c) and (a>b):
#    print(f'en büyük sayı {a}')
#elif (b>c) and (b>a):
#    print(f'en büyük sayı {b}')
#elif (c>a) and (c>b):
#    print(f'en büyük sayı {c}')
#else :
#    print("Bütün sayılar eşit")
#
    
name = input("İsminizi yazınız")
kilo = float(input("Lütfen kilonuzu giriniz"))
    
boy = float(input("Lütfen boyunuzu giriniz"))
  
formul = (kilo) / (boy** 2)
 
print(f'endeks : {formul}')

if (formul> 0) and (formul <= 18.4 ):
   print(f' Sevgili {name} zayıfsınız')
elif (formul> 18.4) and (formul <= 24.9):
   print(f'Sevgili {name} normalsiniz') 
elif (formul> 24.9) and (formul <= 29.9 ):
   print(f'Sevgili {name} fazla kilolusunuz')
elif  (formul> 29.9) and (formul <= 34.9 ):
   print(f'Sevgili {name} obezite şişmanlığındasınız ')
else:
    print("Bilgiler yanlış")


