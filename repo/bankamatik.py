FeyzaHesap = {
    'ad' : 'Feyza Topçu',
    'hesapNo' : '162802039',
    'bakiye' : 20000,
    'ekHesap' : 2000
}

ZeynepHesap = {
    'ad' : 'Zeynep Topçu',
    'hesapNo' : '162802029',
    'bakiye' : 30000,
    'ekHesap' : 2000
}

ReyhanHesap = {
    'ad' : 'Reyhan Topçu',
    'hesapNo' : '162802037',
    'bakiye' : 70000,
    'ekHesap' : 2000
}

EminHesap = {
    'ad' : 'Emin Topçu',
    'hesapNo' : '162802032',
    'bakiye' : 80000,
    'ekHesap' : 2000
}

SuhedaHesap = {
    'ad' : 'Şüheda Topçu',
    'hesapNo' : '162802030',
    'bakiye' : 35000,
    'ekHesap' : 2000
}

def bakiyeSorgulama(hesap):
    print(f" Hoşgeldiniz {hesap['ad']} hesaptaa {hesap['bakiye']} tl var ") 

def paraCekme(hesap,miktar):
    print(f" Hoşgeldiniz {hesap['ad']}")

    if (miktar < hesap['bakiye']):
        hesap['hesap'] -= miktar
        print("Paranızı  çekebilirisiniz")
        bakiyeSorgulama(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekhesapKullanimi = input("Ekhesap kullanmak ister misiniz (e/h)")
            if (ekhesapKullanimi == 'e'):
                bakiye = hesap['bakiye']
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap']-= ekHesapKullanilacakMiktar
                print("Paranız veriliyor . Güle güle kullanın")

            else:
                print("Bakiye yetersiz , iyi günler dileriz")
                bakiyeSorgulama(hesap)
        else:
            print("Bakiye yetersiz üzgünüz ")


paraCekme(FeyzaHesap,40000)
bakiyeSorgulama(FeyzaHesap)
