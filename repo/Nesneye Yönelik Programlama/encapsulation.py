class BankAccount(object):
    
    def __init__(self,name,money,address):
        self.name =name#global
        self.__money = money #private
        self.address = address#global
        
    
     #get and set
    def getMoney(self):
        return self.__money
     
    def setMoney(self,amount):
        self.__money = amount
        
    def __increase(self):
        self.__money = self.__money + 505 
         
p1 = BankAccount("feyza",1000,"barcelona")
p2 = BankAccount("zeynep",2000,"paris")


p1.name
print("get method",p1.getMoney())

p1.setMoney(70000)
p1.getMoney()

p1.__increase()

p1.getMoney()

#%% 

class SonModa(object):
    
    def __init__(self,taki,giysi,esarp):
        self.__taki = taki
        self.giysi = giysi 
        self.esarp = esarp
        
    def getDuzenle(self):
        return self.__taki
            
    def setDuzenle(self,urun):
        self.__taki = urun
        
        
hatun1 = SonModa("gerdanlık","elbise","ipek")

hatun2 = SonModa("bilezik","pantalon","sentetik")



hatun1.esarp

hatun2.getDuzenle()

hatun2.setDuzenle("çeyrek altın") 

hatun2.getDuzenle()       
        
        
        