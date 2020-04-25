
#parent
class Animal :
     def __init__(self):
         print("Animal is created")
         
     def toString(self):
         print("Animal")
         
     def walk(self):
         print("Animal walk")
         

#child

class Monkey(Animal):
    def __init__(self):
        super()
        print("Monkey is created")
        
    def toString(self):
        print("Monkey")
        
    def climb(self):
        print("Monkey can climb")
        
        
        
class Bird(Animal):
    def __init__(self):
        super()
        print("Bird is created")
        
    def toString(self):
        print("Bird")
        
    def fly(self):
        print("Bird fly")
        
        
a1 = Animal()

a1.walk()

a2 = Monkey()
a2.climb()


a3 = Bird()
a3.fly()
