# # file = open("newfile.txt","a",encoding='utf-8')
# # file.write("feyza \n")
# # file.close()

# try :
#     file = open("newline2.txt","r")
# except  FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
# print(file)
file = open("newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i,end="")

#print(file.read(15))
#print(file.readline())
#(file.readlines(),end="")
# liste = file.readlines()
# print(liste[0])
# file.close()

with open("newfile.txt","r",encoding="utf-8") as file :
    content = file.read(10)
    print(content)
    file.seek(15)
    print(file.tell())
    content2 = file.read(10)
    print(content2)


with open("newfile.txt","r+",encoding="utf-8") as file:
   # print(file.read())

with open("newfile.txt","r+",encoding="utf-8") as file:
    file.write("deneme")

with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("newfile.txt","r+",encoding="utf-8") as dosya:
    content = dosya.read()
    content = "emel "+ content 
    dosya.seek(15)
    dosya.write(content)




with open("newfile.txt","r",encoding="utf-8") as dosya:
    print(dosya.read())



with open("newfile.txt","a+",encoding="utf-8") as dosya:
    hebele = dosya.read()
    dosya.seek(25)
    hebele = "ne var " + hebele
    dosya.write(hebele)
   
with open("newfile.txt","r",encoding="utf-8")as dosya:
    print(dosya.read())


#***Syfanın başında güncelleme***#

with open("newfile.txt","r+",encoding="utf-8") as file:
    data = file.read()
    data = "yazııı" + data
    file.seek(0)
    file.write(data)

with open("newfile.txt","r",encoding="utf-8") as dosya:
    print(dosya.read())


***Syfanın ortasında güncelleme***#

with open("newfile.txt","a+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Emin Topçu")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())



