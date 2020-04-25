# def factorial(number):
    
#     def inner_factorial(number):
#         if number <= 1 :
#             return 1
#         return number*inner_factorial(number-1)
#     return inner_factorial(number)


# print(factorial(7))


def hesap(sayi):
    def ic_fact(sayi):
        if sayi <= 1:
            return 1
        return sayi * ic_fact(sayi-1)
    return ic_fact(sayi)


print(hesap(5))