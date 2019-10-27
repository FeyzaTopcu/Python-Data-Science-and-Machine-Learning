degisken = 1
while degisken<10:
    degisken += 1
    if degisken % 2 == 0:
        continue
    print(degisken)


kt = 3

while kt <18:
    kt += 1
    if kt % 3 == 0:
        continue
    if kt == 11:
        break
    print(kt)    


my_flag=True
message = ''

while my_flag:
    message = input('Çıkmak için quit yazın : ')
    if message == 'quit':
        my_flag = False
    else:
        print(message)


my_fast = True
mess= ''

while my_fast:
    mess=input('Çıkmak için yeter yaz :')
    if mess == 'yeter':
        my_fast=False
    else:
        print(mess)



yazi = ''

while yazi !='çık':
    yazi= input('çık yazana kadar bu mesajı göreceksin')
    print(yazi)


nsayi=1
while nsayi<=11:
    print(nsayi)
    nsayi= nsayi +1


dostlar=['kamuran','anil','serhat','beste']

z=0
while (z < len (dostlar)):
    dostt=dostlar[z]
    z=z+1
    if dostt == 'anil':
        continue
    print(dostt)

print("------")


for dost in dostlar:
    if dost == 'anil':
       continue
    print(dost)