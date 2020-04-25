import random
tutulansayi = random.random() 
sayi = int(input('Lütfen bir rakam giriniz : '))

if tutulansayi < sayi:
    sayi = int(input('Lütfen yukarı çıkınız : '))
elif tutulansayi > sayi :
    sayi = int(input('Lütfen bir rakam giriniz : '))

