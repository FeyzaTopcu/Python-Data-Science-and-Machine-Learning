notlar = []

# for i in range(3):
#     name = input("name : ")
#     surname = input("surname :")
#     stdntNo = input("student number : ")
#     nott = input(f' {i+1}. not : ')
#     notlar.append(name,surname,stdntNo,nott)
    
# print(notlar)
def giris():
    print("***** Öğrenci Bilgi Ekranı ********")
    print("1-Not Oku \n 2-Not Gir \n 3-Notları Kayıt Et \n 4-Çıkış")
    istek = int(input("Lütfen yapmak istediğiniz işlemi giriniz:"))
    if istek == 1:
        notOku()
    elif istek == 2:
        notGir()
    elif istek == 3:
        notlariKayitet()
    elif istek == 4:
        notHesapla(5)
    else:
        print("Geçersiz tercih")


def notOku():
    with open("notlar.txt","r",encoding="utf-8") as file:
        for i in file:
            print(i)
       
                
        

def notGir():
    namee = input("name : ")
    surname = input("surname :")
    not1 = input("1.not:")
    not2 = input("2.not:")
    not3 = input("3.not:")
    with open("notlar.txt","a+",encoding="utf-8") as file:
        file.write(namee+ ' ' + surname+ ':'+ not1+ ','+not2+ ','+not3+ "\n")
 

def notlariKayitet():
    with open('notlar.txt',"r",encoding = "utf-8") as file:
        liste = []

        for i in file :
            liste.append(notHesapla(i))
    
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in file2:
                file2.write(i)


def notHesapla(satir):
    satir = satir[:-1]
    liste= satir.split(':')
    print(liste[0])
    print(liste[1])

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1=notlar[0]

    not2= notlar[1]

    not3= notlar[2]

    ortalama = (not1 + not2 + not3)/3



while True:
    giris()


