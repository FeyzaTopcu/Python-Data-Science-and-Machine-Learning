#calculateor project
#class -> init -> method/attribute -> funct vs metod

class Calc(object):
    "calcuator"
    #init metodu
    def __init__(self,a,b):
        "initialize values"
        #attribute
        self.value1 = a
        self.value2 = b
        
        
    def add(self):
        "addition a+b = result -> return result"
        return self.value1+ self.value2  
    
    def multiply(self):
        "multiplication a*b = result -> return result "
        return self.value1 * self.value2
    
    def division(self):
        "division a/b = result -> return result"
        return self.value1/self.value2

v1 =5
v2 =9 
c1 = Calc(v1,v2)

add_result =c1.add()
multiply_result = c1.multiply()

print("add : {}, multiply: {}".format(add_result,multiply_result))
   


    
print("choose add(1), multiply(2), division(3)  ")

selection = input("select 1 or 2 or 3: ")

d1 =int(input("first value :"))

d2 =int(input("second value :"))

c2 = Calc(d1,d2)

addd= c2.add()
multipyy = c2.multiply()
division = c2.division()

if selection == '1':    
    print(addd)

elif selection == '2':
    print(multipyy)
elif selection == '3':
    print(division)
else:
    print("Error there is no proper selection ")