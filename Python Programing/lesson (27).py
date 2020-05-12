def challange(n):
    print(n)
    n = 'feyza'
    print(n)

name = 'feyy'
challange(name)

print(name)

sehirler = ['zonguldak','ankara']

def change(n):
    n[0] = 'kastamonu'

change(sehirler)

print(sehirler)

n = sehirler

n[0] = 'urfa'

print(n)
print(sehirler)

n = sehirler[0:] # slicing

n[0] = 'manisa'

print(n)
print(sehirler)


def add(a,bx,c=0):
    return sum((a,bx,c))

print(add(4,7))

def added( *deger):
    return print(sum ((deger)))

added(7,9,8,5,2,4,1)

def eklereis(*arg):
    sum = 0

    for i in arg:
        sum = sum + i
    print(sum)

eklereis(8,9,5,41)

def hoppala(**args):
    for key,value in args.items():
        print(f' {key} is {value}')


hoppala (namme = 'Emin', age = 61, city = 'Çankırı')
hoppala (namme = 'Zeynep', age = 58, city = 'Karabük')
hoppala(namme = 'Şüheda' , age = 30, city = 'Zonguldak')
hoppala(namme = 'Reyhan' , age = 28, city = 'Zonguldak')
hoppala(namme = 'Feyza' , age = 22, city = 'Zonguldak')

hoppala()


def denebakiim(a,b,*arg,**args):
    print(a)
    print(b)
    print(arg)
    print(args)


denebakiim(87,96,56,12,45,52,32,13, key1 = 'feyzık', key2 = 'tospik')


