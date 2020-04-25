result = " neber moruk iyiyin mi ?"

length = len( result )
print(length)

sonuc = result[4: 18] 
print (sonuc )

sonuc = result[ :: -1 ]  # tersten yazdırır
print (sonuc )

name, surname , age , job = "feyza" , "topçu", 55 , "mühendis"

soz = "benim adim"+ name + surname + " yaşım" + str(age) + job

print(soz)

soz = 'benim adım {2} {1} , yaşım {0} ve mesleğim {3} ' .format(name,surname,age,job)

print(soz)

soz = "benim adım {name} {surname} yaşım  {age} mesleğim {job}"

s = 'hello world' 
s = s[0:6] + 'W' + s [-4:]
print(s)
s.replace('w','W')

k = 'abc ' * 3 
print(k)