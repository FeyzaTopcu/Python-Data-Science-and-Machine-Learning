def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_Adi):
    if islem_Adi == "toplama":
        print(f1(2,3))
    elif islem_Adi == "cikarma":
        print(f2(5,3))
    elif islem_Adi == "carpma":
        print(f3(6,2))
    elif islem_Adi == "bolme":
        print(f4(18,3))
    else:
        print("Geçersiz işlem...")

islem(toplama,cikarma,carpma,bolme,"cikarma")
islem(toplama,cikarma,carpma,bolme,"toplama")

islem(toplama,cikarma,carpma,bolme,"carpma")
islem(toplama,cikarma,carpma,bolme,"bolme")


islem(toplama,cikarma,carpma,bolme,"hesap")

