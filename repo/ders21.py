def  sayHello ():
    print("günaydın")


sayHello()


def rakam():
    print("olaylar karışık müdür")

rakam()


def merhabade(name):
    print(f'{name} merhaba ')


merhabade("feyza")


def topla(sayi1, sayi2):
    return sayi1 + sayi2
    
 

print(topla(15,12))


def yasHesaplama(yil, namee):
    dogumgunu = 2020- yil
    print(f'Sevgili {namee} yaşınız {dogumgunu}')

yasHesaplama(1997, 'feyza')

def emeklilik(yas,isim) :
    '''
    yil ve isim onemli
    '''
    emekli= 65 - yas
    print(f'{isim} emeliliğe {emekli} yıl var')


print(help(emeklilik))






    