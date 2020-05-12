class Student :

    test= 'test ettir'
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student1=Student('mahmut',33,[14,50,90,55])
student_2= Student('fatma', 25,[42,56,32,88])

class UniversityStudent(Student):
  
    def __init__ (self,name,age,grades,university):
        super().__init__(name,age,grades)
        self.university= university


u_student1 = UniversityStudent('feyza',21,[10,20,30],'CBU')


print(u_student1.age)
print(u_student1.name)
print(u_student1.average())

print(u_student1.university)
print(u_student1.average())


print(Student.test)
print(UniversityStudent.test)


print("---------------")



class  Circle:
    pi=3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius*self.pi

    def __len__(self):
        return self.radius * self.radius


    def __repr__(self):
        return f'{__class__.__name__} nesnesi ve yarıçapı {self.radius}'


Circle_1=Circle(5)
print(Circle_1)

print(Circle_1.__repr__())

print(dir(Circle_1))

print(len(Circle_1))
print(dir(Circle_1))

#print(4+8) == print(int.__add__(4,8))