#error handling => hata yönetimi

try:
    x = int(input('x : '))
    y = int(input('y : '))
    print(x/y)
except Exception as ex:
    print('yanlış bilgi girdiniz',ex)
else:
    pass

finally:
    print('try exception sonlandı')
