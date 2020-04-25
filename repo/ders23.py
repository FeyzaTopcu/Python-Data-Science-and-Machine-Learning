def square(num): return num **2

print(square(5))


nubers = [2,3,6,7,8]

print(list(map(square,nubers)))


for i in map(square,nubers):
    print(i)

sehir = ["sinop","mersin","kastamonu"]

def isimgoster(isim): return print("efsane bir yer "+isim)

print(list(map(isimgoster,sehir)))

for k in map(isimgoster,sehir):
    print(k)



result = list(map(lambda numara : numara**2,nubers))
print(result)

result= list(map(lambda hayat: hayat * 23 , nubers))

print(result)


result = list(map(lambda r:( r**9 )+23 , nubers))
print(result)
def cift(sayi):
    if sayi % 2 == 0:
        print(sayi)

def tek(sayi):
    if sayi % 2 == 1:
        print(sayi)

result = list(filter(cift,nubers))

result= list(filter(tek,nubers))
print(result)

result = list(filter(lambda b : b % 2 == 0, nubers))
print(result)