#class

class Person :
    #class attributes
    adress = 'no information'
    #constructor (yapıcı metod)
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı ')

     #instance methots
    def intro(self):
        print('Hello there '+self.name)

    def calculatingAge(self):
        return 2020 - self.year

#object (instance)
p1 = Person('feyza', 1997)
p2 = Person('Reyhan', 1992)

#updating 

p1.name = 'şüheda'

p1.year = 1989

#accessing object attributes

print(f'p1: name : {p1.name} year : {p1.year} adress: {p1.adress}')
print(f'p2: name : {p2.name} year : {p2.year} adress : {p2.adress}')

print(p1)
print(p2)

print(type(p1))
print(type(p2))
p1.intro()
p2.intro()
print(p1.calculatingAge())