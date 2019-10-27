class Student:
    def __init__(self,fullname,name,surname,age,grades):
        self.name=name
        self.surname=surname
        self.age=age
        self.grades=grades

    def average(self):
        return sum(self.grades)/ len(self.grades)

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

student_1 = Student('tolga','yazilim',22,[5,4,55])

print(student_1.name)
print(student_1.surname)
print(student_1.average())
print(student_1.fullname())


student_1.name='feyza'

print(student_1.name)
print(student_1.surname)
print(student_1.average())

print("----------")


class Dog:
    def __init__(self,name):
        self.name=name

    def myname(self):
        print(f'benim adım {self.name}')


dog1 =Dog('tom')
dog1.name='jo'
print(dog1.name)

class Person :
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age

    def __str__(self):
        return self.name + '' +self.surname + ''+str(self.age)


class Employee(Person):
    def __init__(self,name,surname,age,salary):
        super().__init__(name,surname,age)
        self.salary=salary

    def __str__(self):
        return super().__str__()+''+str(self.salary)

employee1=Employee('feyza','topçu', 21,10000)

print(employee1.salary)
print(employee1.__str__())