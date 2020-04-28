# def usalma(number):

#     def inner(power):
#         return number ** power

#     return inner


# two = usalma(2)
# print(two(2))
# pr = usalma(3)
# print(pr(3))

# print(usalma(3))

# four = usalma(4)
# print(four(5))


def yetki(page):
    def mevki(rol):
        if rol == 'Admin':
            return "{0} rolü {1} sayfasına ulaşabilir.".format(rol,page)
        else :
            return "{0} rolü {1} sayfasına ulaşamaz".format(rol,page)
    return mevki


user1= yetki("Devops Page")
user2 = yetki("Data Scientist Page")
user3 = yetki("Cyber Security Page")

print(user3("Admin"))
print(user2("User"))
print(user1("Admin"))


def islem(islemIsmi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carp = 1
        for i in args:
            carp*=i
        return carp

    if islemIsmi == "carpma":
        return carpma
    else:
        return toplama

toplama = islem("toplama")
print(toplama(7,8,9))


carpma = islem("carpma")
print(carpma(4,5,87))
