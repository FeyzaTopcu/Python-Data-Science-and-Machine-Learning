list1 = ['one', 'two', 'three']

list2 = ['four','five', 'six']
numbers = list1 + list2
print(numbers[4]) 

userA = [' feyza ', 45]

userB = ['çınar' , 56]

users = [ userA , userB]

print(users)
print(users[1][0])

list1[-1] =  'hayırlısı'
print(list1)

list3 = 'hayırlısı' in list1
print(list3)

list2[-2 : ] = 'sus' , 'konuşma' 
print(list2)

user = users + ['gel', 'gitme'] 
print(user)

studentA = ['feyza', 'topçu',2010,[80,56,96]]
studentB = ['sena','Turan',2020,[45,85,22   ]]
studentC =  ['gamze','kaya',2015,[74,56,69]]

deger = f'benim adım {studentA[0]} {studentB[3][2]} yaşındatım ortalamam {(studentA[3][0]+studentA[3][1]+ studentA[3][2])/3}' 

print(deger)
list2.append('ne var')
list1.insert(2,'nolmuş')

print(list1, list2)

list2.pop()
print(list2)

list1.remove("one")

f= [1,5,6,3]
f.sort()
print(f)
