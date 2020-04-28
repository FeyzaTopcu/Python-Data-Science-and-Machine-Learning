girilen_deger = []

for i in range(0,2):

    i = input('deger giriniz')
    girilen_deger.append(i)
    
if girilen_deger[0] > girilen_deger[1]:
 print("maximum olan sayı: " + girilen_deger[0])

else:
  print("maximum olan sayı: " + girilen_deger[1])

print('*'*50)

vize1 = float(input('1. vize'))
vize2 = float(input('2. vize'))

final= float(input('final'))

ort= ((vize1+ vize2)*0.3) + (final*0.4)
print(f"not ortalamanız: {ort} geçme durumu  {ort>50} ")

print("*"*50)
sayi =int(input("sayı giriniz :"))
tekcift = sayi % 2 == 0
print(f"girien sayı çift mi {tekcift}")

print("*"*50)
sayi2 = int(input("sayi giriniz "))

pozitifmi = (sayi2 > 0)

print(f"sayi pozitiflik durumu {pozitifmi}")


mail = "feyza@gmail"
parolaa = "ab12"

email = input("mail adresiniz")

parola = input("parolanız ")

k = (mail == email)
z = (parolaa == parola)
print( f"girilen mail {k} ve parola {z}")




