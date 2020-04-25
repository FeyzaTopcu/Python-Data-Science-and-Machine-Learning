# def greeting(name):
#     print('hello',name)

# greeting("feyza")

# sd = greeting

# print(sd)
# print(greeting)
# print("*"*50)
# print(greeting("feyza"))
# print("*"*50) 

# #encapsulation   
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1+1
    
#     num2 = inner_increment(num1)
#     print(num1,num2)

#     def total(num1):
#         print("total")
#         return num1 * num1
#     num3 = total(num1)
#     print(num1,num3)


# outer(10)


def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")

    if not number <=0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1 :
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)

try:
    print(factorial("-2"))
except Exception as ex:
    print(ex)
    
