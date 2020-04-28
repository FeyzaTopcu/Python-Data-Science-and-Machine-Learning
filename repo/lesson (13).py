ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı : ")
surname = input("öğrenci soyadı : ")
phone = input("öğrenci telefon : ")

#ogrenciler[number] = {
#    'name' : name,
#    'surname': surname,
#    'phone': phone
#
#}
#print(ogrenciler)
ogrenciler.update({
     number: {
            'ad' : name,
            'soyad': surname,
            'phone': phone 
        }
    
})

print('*' * 50 )

ky= input("öğrenci no :")
ogrenci= ogrenciler[ky]
print(ogrenci)

print(f"öğrencinin adı {ogrenci['ad']} soyadı {ogrenci['soyad']} okul numarası {ky} telefon numarası {ogrenci['phone']}")