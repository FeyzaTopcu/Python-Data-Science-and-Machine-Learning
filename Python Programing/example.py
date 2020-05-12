name = input("isminiz: ")
age = int(input("yaşınız : "))
egitim = input("eğitim durumunuz: ")

if(age > 18 and (egitim == "üniversite " or egitim== "lise")):
    print("ehliyet alabilirsiniz")
else:
    print("ehliyet alamazsınız")

print("*"*50)
yazili= []
for i in range(2):
    i= int(input("yazili notu :"))
    yazili.append(i)

sozlu = int(input("sözlü  notu : "))

deger= (yazili[0]+ yazili[1]+sozlu)
ort= deger/3
print(ort)
if(ort>0 and ort<24):
    print("notunuz 0")

elif(ort> 24 and ort<44):
    print("notun 1")
elif(ort>45 and ort<54):
    print("notun 2")
elif(ort>55 and ort<69):
    print("notun 3")

elif(ort>70 and ort<84):
    print("notun 4")
elif(ort>85 and ort<=100):
    print("notun 5")
days = int(input("aracınjız kaç gündür serviste ?"))

if days<= 365:
    print("1. servis aralığı ")
elif days > 365 and days<=365*2:
    print("2. servis aralığı ")

elif days > 365*2 and days<=365*3:
    print("3. servis aralığı ")

else:
    print("hatalı süre")

import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (YYYY/AA/GG):')

tarih = tarih.split('/')

trafigeCikis= datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
print(trafigeCikis)
fark =  simdi - trafigeCikis
days = fark.days


if fark <= 356:
    print('1. servis aralığı')
elif days > 365 and days <= 365*2:
    print('2. servis aralığı')
elif days*2 and days <= days*3:
    print('3. servis aralığı')
else :
    print('hatalı süre')