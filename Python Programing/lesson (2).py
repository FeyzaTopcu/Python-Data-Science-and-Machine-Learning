import os

result = dir(os)

print(result)

result = os.name #kullanılan işletim sistemi adını gösterir

print(result)

result = os.getcwd()  #bu dosyanın bulunduğu dizini gösterir

print(result)


os.chdir('E:\\')


#os.mkdir("Yeni dizin")

result = os.getcwd()
print(result)

os.chdir('E:\Python')

print(os.getcwd())

os.chdir('..')  #dizin değiştirme

print(os.getcwd()) #bulunduğun dizini öğrenme

#os.makedirs("neww/dosya") #klasörün içine oluştur

#listeleme işlemleri

result = os.listdir('E:\\Python')

print(result)


for dosya in os.listdir():
    if dosya .endswith('.py'):
        print(dosya) 
os.chdir('E:Python')
print(os.getcwd())
result = os.stat("ders44.py")
print(result)

#result = result.st_size/1024
import datetime

# result = datetime.datetime.fromtimestamp(result.st_ctime)#oluşturulma tarihi
# result =datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi

#result = datetime.datetime.fromtimestamp(result.st_mtime) #değiştirilme tarihi

os.system("Dev-C++.exe")

print(result)

# os.rmdir("neww")


result = os.path.abspath("ders44.py")


result = os.path.dirname("E:/Python/ders44.py") #verilen dosyanın yolunu bulur. 

result = os.path.dirname(os.path.abspath("ders44.py"))

result = os.path.exists("E:/Python/ders444.py") #verilen konumda o dosya var mı  

result = os.path.isdir("E:/Python/ders44.py") #klasör mü kontrolü

result = os.path.join("E:\\","dene")

result =  os.path.splitext("ders44.py")

result = result[0]

result = result[1]

result = os.path.split("E:/Python/ders44.py")

print(result)