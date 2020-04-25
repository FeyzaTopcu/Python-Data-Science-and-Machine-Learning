#liste = ["1","2","3a","10b","abc","10","50"]
#
#for i in liste:
#    try:
#        result = int(i)
#        print(result)
#
#    except Exception as ex:
#        continue
#
#    
#
#    
#kelime = ["feyza","reyhan","68","şüheda","emin","zeynep"]
#
#for i in kelime:
#    try:
#       result = int(i)
#       print(result)
#    except Exception :
#        continue
# 
#
#
#while True:
#    t = input('rakam gir')
#    if  t == 'q':
#        break
#    try:
#        result = float(t)
#        break
#    except ValueError:
#        print('geçersiz sayı ')
    #   continue
    


#turkce = 'şçğıöüİ'
#parolaa = input("parola gir : ")
#
#def parola(pswd):
#
#    for i in parolaa:
#        if i in turkce:
#            raise TypeError('Parola türkçe karekter içeremez')
#        else:
#            pass
#    print("geçerli parola : ",pswd)    
#
#parola(parolaa)




#keli= input("kelime gir")
#def bul(klm):
#    kelime = 'slk'
#    for i in keli:
#        if i in kelime:
#            raise TypeError("bunları yazma")
#        else:
#            pass
#
#    print("öyle işte")
#
#bul(keli)


def faktoriyel(x):

    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer')
        

    result = 1

    for i in range(1,x+1):
        result *= i

    return print(result)



faktoriyel(5)
for x in [5,7,-3,-4,54]:
    try:
        faktoriyel(x)
    except ValueError as ex:
        print(f' {x} sayısı ',ex )
        continue