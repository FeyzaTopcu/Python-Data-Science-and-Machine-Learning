# -*- coding: utf-8 -*-
"""


@author: FEYZA
"""

integer = 22
string = "feyza"
 
# %% classes

employee = "zeynep"
employee_age = 59
employee_adres = "ankara"

class Employee(object):
    #attribute = age,adress,name
    #behaviour = yapabildiği özellikler
    pass

employee1 = Employee()

#%%

class Footballer:
    age = 30
    football_club = "barcelona"

f1 = Footballer()

print(f1.age)
print(f1.football_club)

f1.football_club = "real madrid"


f1.football_club

#%%
class Square(object):
    
    edge = 5 #meter
    area1 =7
    def area(self):
    
        self.area1 = self.edge * self.edge
        print("area :",self.area1)

s1 = Square()

print(s1)
print(s1.edge)
 
s1.area()



#%%
class Exmpl(object):
    
    speaking_number = 5
    one_weak= 7
    
    def speak(self):
        total = self.speaking_number* self.one_weak
        print(f'total : {total}')
        

ex1 = Exmpl()

ex1.speak()
# %% Methods vs function


class weed(object):
    weed_num= 5
    
    def caculate(self):
        
        total = self.weed_num*24
        print(f'total weed : {total}')


w1 = weed()

w1.caculate()

#%%

class Emp(object):
    
    age =25
    salary = 1000 
    def ageSalaryRatio(self):
        return (self.age* self.salary)
    
def ageSalaryRatio(age,salary):
    return (age/salary)

e1 = Emp() 
e1.ageSalaryRatio()


ageSalaryRatio(45,5)

pi =3.15

def findarea(pi,r):
    area = pi*r**2
    return area

findarea(pi,5)


value1 = findarea(pi,8)

value2 = findarea(pi,7)

print(value1+value2)


# %%
class Animal(object):
   def __init__(self,a,b):
       self.name = a
       self.age = b
       
   def getAge(self):
       return self.age
    
   def getName(self):
       return(self.name)
        
a1 = Animal("dog",3)
a2 = Animal("cat",1)
a3 = Animal("bird",2)
        
a1.getAge()
        
a1.getName()
        
a2.getName()

a2.getAge()
        
        
        
        
        
         