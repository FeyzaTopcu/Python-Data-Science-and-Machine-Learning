class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year= year

    def brandmodel (self):
        return f'Araba markası {self.brand} ve model {self.model}'

car_1 = Car('BMW','i5',2010)
car_2= Car('Audio', 'x6',2012)


print(car_1)
print(car_1.brand)
print(car_1.brandmodel())


print("-------------------------")

class Movie:
    def __init__(self, name, directior):
        self.name = name
        self.directior= directior

movie_1 = Movie('Full Metal Jacket', 'Kubrick')
movie_2 = Movie('Babel', 'Irarutu')


print(movie_1.directior)
print(movie_2.directior)

print("-------------------------")

class Student:
    school_name='X Lisesi'
    number_of_student = 0
    def __init__(self,name,age,grades):
        self.name=name
        self.age= age
        self.grades = grades
        Student.number_of_student +=1

    def avarage(self):
        return sum(self.grades) / len(self.grades)

    def SchoolName(self):
        return f'Okulumuzun adı {self.school_name}'

    @classmethod
    def display_school_name(cls,name_of_school):
        cls.school_name= name_of_school

    @staticmethod
    def statik():
        return f'Sadece yazı yazdım '


Student.display_school_name('Y Lisesi')

print(f'öğrenci numarası : {Student.number_of_student}')



student_1 = Student('mahmut',33,[14,50,90,55])
student_2= Student('fatma', 25,[42,56,32,88])

print(student_1.avarage())
print(student_2.avarage())

student_1.name='feyza'
print(student_1.name)

student_1.school_name='Z Lisesi'

print(student_1.school_name)
print(student_2.school_name)
print(Student.school_name)

print(student_1.SchoolName())


print(Student.__dict__)


print(f'öğrenci numarası : {Student.number_of_student}')

print(student_2.statik())