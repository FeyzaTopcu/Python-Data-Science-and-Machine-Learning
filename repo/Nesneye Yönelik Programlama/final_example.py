
from abc import  ABC,abstractmethod

#inheritance
class Shape:
    
    """
    Shape = super class /abstract class
    """
    #abstract method
    @abstractmethod
    def area(self):pass
    @abstractmethod
    def perimeter(self):pass

    #overriding and polymorphisim
    def toString(self):pass


#child
class Square(Shape):
    """ sub class  """
    def __init__(self,edge):
        self.__edge= edge #encapsulation private attribute
        
    def area(self):
        return print(self.__edge ** 2)
     
    def perimeter(self):
        return print(self.__edge *4)

    def toString(self):
        print("**Square EDGE : **",self.__edge)
        
#child        
class Circle(Shape):
    
     """circle class """
     #constant variable
     PI = 3.14
     
     def __init__(self,r):
        self.__r= r #encapsulation private attribute
        
     def area(self):
        return print(self.PI *self.__r**2)
     
     def perimeter(self):
        return print(self.__r*self.PI*2)

     def toString(self):
        print("**Circle Radius : **",self.__r)    


s1 = Shape()
s2 = Square(5)
c1 = Circle(4)

s1.area()
s1.perimeter()
s1.toString()


s2.area()
s2.toString()
s2.perimeter()

c1.area()
c1.perimeter()
c1.toString() 


       