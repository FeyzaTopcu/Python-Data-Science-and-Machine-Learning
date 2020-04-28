def my_decorater(func):
    def wraper(name):
        print("fonksiyondan önceki işlemler")
        func(name )
        print("fonksiyondan sonraki işlemler")
    return wraper

@my_decorater
def sayHello(nesne):
    print("hello",nesne)

sayHello("tabak")

import math 
import time

def caclculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon "+ func.__name__+str(finish-start)+ " saniye sürdü")
    return inner

@caclculate_time
def usalma(a,b):
    
    print(math.pow(a,b))

@caclculate_time
def faktoriyel(num):

    print(math.factorial(num))
   

usalma(5,7)

faktoriyel(8)

@caclculate_time
def toplama(a,b):
    return print(a+b)


toplama(78,56)
