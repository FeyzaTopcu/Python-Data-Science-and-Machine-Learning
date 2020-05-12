list1=[]
list2= list()

print(type(list1))

print(type(list2))


tuple1 = ()
tuple2 = tuple()


print(type(tuple1))

print(type(tuple2))

set2= set()
print(type(set2))

dict1= dict()
dict2= {}
print(type(dict1))
print(type(dict2))


sozlukk= {'deniz': 15, 'mert': 85, 'gamze': 74}
print(sozlukk['deniz'])
print(sum(sozlukk.values())/(len(sozlukk.values())))

sozlukk['huseyin']=78
print(sozlukk)

sozlukk.update({'huseyisdsd': 95})
print(sozlukk)

sozlukk.pop('huseyisdsd')
print(sozlukk)



karisik= {'deniz': [15,45,89] ,'mert': [85,96], 'gamze':[85,96, 74],'ymze':[85,96, 74]}


karisik['deniz']= [karisik['deniz'][1]**2 ,karisik['deniz'][2]**2,karisik['deniz'][2]**2  ]
print(karisik)

yorum={'values': [1,2,3,4,5,6,7,8,9,10,11,12,13]}

for v in yorum.values():
    my_list=[]
    for s in v:
        my_list.append(s**2)

yorum['values']= my_list

print(yorum)

diff= {'deniz': [15,45,89] ,'mert': [85,96], 'gamze':[85,96, 74],'ymze':[85,96, 74]}
ddg=[]
for g in diff.keys():
   ddg.append(g)

print(ddg)

diff= {'deniz': 15 ,'mert': 85, 'gamze':885,'ymze': 74}

ssa=[]
asd=[]

for h,s in diff.items():
    ssa.append(h)
    asd.append(s)

print(ssa)
print(asd)

print(sum(asd))


numberr= {x : x**2 for x in range(1,11)}
print(numberr)


harf= {d :d**3 for d in range(7,9)}
print(harf)