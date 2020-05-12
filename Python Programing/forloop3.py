num = int(input('lütfen bir sayi giriniz'))

if num < 0:
    print('Negatif bir sayi girdiniz')

else:
    sum = 0
    while num > 0:
        sum +=num
        num -= 1
    print(f'toplam sayi : {sum}')




calcius = [20,30,0,50,60]
kelvin= []
fahrenheit= []

for c in calcius:
    k= c + 273
    kelvin.append(k)
    f = c*9/ 5 + 32
    fahrenheit.append(f)

print(f' kelvin : {kelvin}')
print(f'fahrenent : {fahrenheit}')



import random 
xnum = random.randint(1,100)

num = int(input('Lütfen 1 ile 100 arasında bir sayı giriniz'))

while num != xnum:
    if num < xnum:
        print(f'Lütfen {num} dan daha büyük bir sayi giriniz')
        num=int(input('sayi : '))
    elif num > xnum:
          print(f'Lütfen {num} dan daha küçük bir sayi giriniz')
          num=int(input('sayi : '))
    else:
       print(f'Tebrikler {num} sayısını buldunuz')


print(f'sistemin tuttuğu sayi :  {xnum} ')




maxNum = int(input('Lütfen maximum girebileceğiniz bir  sayı giriniz'))
minNum = int(input('Lütfen minimum girebileceğiniz bir sayı giriniz'))

for evenNum in range(minNum,maxNum):
    if evenNum % 2 == 0:
        continue
    else:
        print(evenNum)