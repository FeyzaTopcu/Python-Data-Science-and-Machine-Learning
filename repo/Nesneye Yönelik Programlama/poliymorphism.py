
class Brand():
  
    def Information(self):
         brand_number = 80
         worker_number = 2000
         product_number = 17000
         print(brand_number,product_number,worker_number)
         
         
class Nike(Brand):
    def Information(self):
         product_number =7
         worker_number = 200
         print(product_number,worker_number)
           
         
class Adidas(Brand):
    def Information(self):
        product_number =7
        worker_number = 200
        print(product_number,worker_number)
                       
               
                 
b1 =Brand()
b1.Information()

n1 =Nike()
n1.Information()

a1 = Adidas()
a1.Information()