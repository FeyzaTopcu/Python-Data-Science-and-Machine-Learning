cities= ['antep','urfa','maras','trabzon']

for city in cities:
    print(f'gezilen sehir: {city}')

st= 'feyza*topcuyazılım*mühendimy_list'

myy= st.split('*')
print(myy)

ss='dsdsd@gdgdgd'
m=ss.split('@')
print(m)

for number in range (1,10):

    print(number)
num = list(range(1,8))
print(num)


num =list(range(40,50))


numb= [number for number in range(2,12) ]
print(numb)

dizi=['feef',['dfdf','sdsf','dstgeg'],'yrte','rtyfg']

ct= dizi[:2]
print(ct)
print(dizi[-2:])

print(dizi[1][2])

print(dizi[len(dizi)-1])

dizi[len(dizi):] = ['sdfsfdfsdsda']
print(dizi)

dizi.insert(len(dizi),'hdhdgsg')
print(dizi)


dersler= [['mat','kimya'],['fizik','geo','bio'],['beden','muzik','din k.'] ]

ge = []
for ders in dersler :
    ge.append(ders[-0])
    print(ge)



squares = []
for num in range(1,11):
    squares.append(num**2)

print(squares)

sq= [num**2 for num in range(1,8)]
print(sq)
d= [n**3 for n in range(4,9)]
print(d)

print(len(d))
print(d[2:4])

dd= ('de','me','ole')

for ddsa in dd :
    print(ddsa)


dds= {'melike','zisan','bahar','cagla'}
dds.add('feyza')
print(dds)

tyr=list(dds)
print(tyr)

stringg='rtyuihgfd'
sset={harf for harf in stringg}
print(sset)