#x = 10

#if x > 5 :
#    raise Exception(" x 5 den büyük değer")

#y= 78

#if y>7:
 #   raise Exception(" y 70 den büyük olmamalıdır.")

#t=45

#if t > 44:
   # raise Exception("t 44 den büyük olamaz")

def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 7 karekter olmalı")
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermelidir")
    elif not re.search("_@$",psw):
        raise Exception("parola özel karekterler içermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam içermelidir")
    else:
        print("geçerli parola ")

password = "12345678aA$"
try: 
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("geçerli parola: else")

finally:
    print("validation tamamlandı")


class person :
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("name alanı fazla karekter içeriyor")
        else:
            self.name = name

p= person("Feyzaaaaaaaa",1997)