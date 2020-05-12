def karesi (x):
    return x**2


x = int(input('Lütfen bir sayı giriniz'))

print(f'girilen {x} sayisinin karesi {karesi(x)}')



p = int(input('Lütfen bir p sayısı giriniz'))

s = int(input('Lütfen bir s sayısı giriniz'))

carp=lambda p,s: p*s
topla = lambda p,s: p+s

print(f'{p} ve {s} nin çarpımı : {carp(p,s)}')


print(f'{p} ve {s} nin toplamı : {topla(p,s)}')




def multiply(my_list):
    mult=1
    for num in my_list:
        mult*= num
    return mult

list=[4,8,5,6,3]

print(multiply(list))



def deneme(mylist):
    sayac=1
    for i in mylist:
        sayac*=i
    return sayac
lisst=[23,45,67,89]

print(deneme(lisst))



def carpalim(listem):
    sayac=1
    for h in listem:
        sayac *= h
    return sayac

liste= [7,8,71,9,4,1]
print(carpalim(liste))


def toplayalim(listt):
    sayac=0
    for i in listt:
        sayac +=i
    return sayac

listele=[18,28,8]
print(toplayalim(listele))



a = int(input('Lütfen faktoriyeli hesaplanacak sayıyı giriniz'))
def faktoriyel (a):
 
    if a == 0:
        return 1
    else:
        return a* faktoriyel(a-1)



print(faktoriyel(a))



def hacim(b):
    return 12*(b**3)

def alan(b):
    return 12* (b**2)
b = int(input('Lütfen faktoriyeli hesaplanacak sayıyı giriniz'))

print(f'Bir kenarı {b} olan bir küp\'ün hacmi {hacim(b)}, alanı {alan(b)}')


xy='global level'

def enclosing():
    xy= 'enclosing level'
    def innerfunc():
        xy='local level'
        print(xy)
    innerfunc()

enclosing()