 #Inheritance(Kalıtım) : Miras Alma

 #Person => name,lastname,age,eat(),drink()

 #Student(Person), Teacher(Person)

 #Animal => Dog(Animal), Cat(Animal)


class Person():
    def __init__(self,fname,lname):
        self.name = fname
        self.lastname =lname

        print('Person Created')
   
    def eat(self):
        print("Yemekler yenildi")


    
class Student(Person):
    print("*"*20)
    
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        Person.eat(self)

        print("Student created")
#

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch
        Person.eat(self)

    def who_I_am(self):
        print(f' Ben {self.branch} öğretmeniyim')


p1 = Person('Şüheda','Topçu')
s1 = Student('Emin','Topçu')
#p2 = Person('Reyhan','Topçu')
#s2 = Student('Zeynep','Topçu')
t1 = Teacher('Aslı','Kara','Matematik')

print(p1.name + '' + p1.lastname)
print(s1.name + '' + s1.lastname)

t1.who_I_am()