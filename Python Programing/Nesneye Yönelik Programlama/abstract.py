from abc import ABC,abstractmethod

class Animal(ABC): #super class
     
    @abstractmethod
    def walk(self):
        print("walk")
    @abstractmethod
    def run(self):
        print("run")
        
class Bird(Animal):  #sub class
    
    def __init__(self):
        print("bird")
    
    def walk(self):
        print("walk")
    
    def run(self):
        print("run")
        
b1 =Bird()
b1.run()
b1.walk()