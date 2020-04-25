x = 0
while x <= 100:
    if  x % 2 == 0:
        print(f'{x} çifttir')
    else:
        print(f'{x} tektir')
    x += 1
print("Bitti...")

name ='' #False

while not name.strip() :
    name= input("İsminiz")

print(f'Merhaba {name}')
