import sqlite3

class Product:
    def __init__(self,name,brand,price,kind,expiration_date,stock):
        self.name = name
        self.brand = brand
        self.price =price
        self.kind = kind
        self.expiration_date = expiration_date
        self.stock = stock

    def __str__(self):      #print fonksiyonunun stoğu geri döndürmesini sağlıyoruz.
        return self.stock


class SuperMarket():

    def __init__(self):
        self.ConnectDatabase()

        self.firsLogin = True #init fonksiyonu ilk çalışan fonksiyon olduğu için buraya yazdım. programın başında çalışmasını istiyorum.
        self.dailyTotalCustomer = 0 #init fonksiyonu ilk çalışan fonksiyon olduğu için buraya yazdım. programın başında çalışmasını istiyorum.
        self.totalPrice =0 #init fonksiyonu ilk çalışan fonksiyon olduğu için buraya yazdım. programın başında çalışmasını istiyorum.
        self.totalCiro=0 #init fonksiyonu ilk çalışan fonksiyon olduğu için buraya yazdım. programın başında çalışmasını istiyorum.
        self.dailyTotalreturn =0

    
    def ConnectDatabase(self):
        self.connect = sqlite3.connect("product.db")
        self.cursor = self.connect.cursor()

        select = "CREATE TABLE IF NOT EXISTS products (name TEXT,brand TEXT,price REAL,kind TEXT,expiration_date DATE,stock INT)"

        self.cursor.execute(select)
        self.connect.commit()

    def DisconnectDatabase(self):
        self.connect.close()

    
    def Add_Product(self,product_object):
        query = "INSERT INTO products VALUES(?,?,?,?,?,?)"
        self.cursor.execute(query,(product_object.name,product_object.brand,product_object.price,product_object.kind,product_object.expiration_date,product_object.stock))
        self.connect.commit()

    def Delete_Product(self,name):

        # sorguyu DELETE 'in altında yapılsaydı,sorgu bulup sildiği için query2 sistemde bulamadığı için Her seferinde if'e girecekti.
        # Bunu üstte yazarsak önce veritabanını sorgulayacak if veya else girip alttaki query2'den devam edecek.
        # DELETE işlemi, veritabanında bulunsada bulunmasada hata vermeden devam eder. Varsa siler yoksa hatasız devam eder.

        query2 = "SELECT * FROM products WHERE name = ? "
        self.cursor.execute(query2,(name,))
        deleteProduct = self.cursor.fetchall()

        if (len(deleteProduct)== 0):
            print("There is no such product.")
        else:
            print("Product is deleted !!!") 

        query = "DELETE FROM products WHERE name = ?"
        self.cursor.execute(query,(name,))
        self.connect.commit()

    def NameofqueryStock(self,name):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query,(name,))
        products = self.cursor.fetchall() #veri tabanındaki bulunan ürünleri çekiyorum

        if (len(products) == 0):
            print("There is no such product")
        else:
            totalProduct =0
            for i in products:
                totalProduct += i[5]  ##Aynı ürünü sonradan birdaha eklemiş olabilirim. Bu products listesinin içine atanır.
                                      #Bu yüzden products listesini for ile geziyorum. hepsinin 5.indeksindeki stock verisine erişip,
                                      #o değeri toplamurun değişkenine atayarak topluyorum.

            print(totalProduct)  #en sonda totalProduct'ı yazdırıyorum.
    def BrandofqueryStock(self,brand):

        query = "SELECT * FROM products WHERE brand = ?"
        self.cursor.execute(query,(brand,))
        brand_product = self.cursor.fetchall() #veri tabanında bulunan ürünleri çekiyorum

        if(len(brand) == 0):
            print("There is no such brand product in stock")

        else:
            totalBrandproduct =0

            for i in brand_product:
                totalBrandproduct += i[5]
                print(f' {brand} for brand product in total {totalBrandproduct}  ')

    def TotalProductStock(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        totalstock = self.cursor.fetchall()

        if(len(totalstock) == 0):
            print("No products in stock ")
        else:
            total_product_stock = 0

            for i in totalstock:
                total_product_stock += i[5]
                print(f'Total product in stock {total_product_stock}')

    def DeleteExpired(self,name):
        query ="DELETE  FROM products WHERE name = ?  "
        self.cursor.execute(query,(name,))
        self.connect.commit()

    def ProductRemoveExpiration(self,date):
        query = "SELECT * FROM products "
        self.cursor.execute(query)
        removeexpiration = self.cursor.fetchall()

        if(len(removeexpiration) == 0):
            print("No product has expired ")
        else:
            for i in  removeexpiration:
                expiration_date_list = i[4].split(".")  #i.demetin 4.elemanı  expiration_date idi. Bunu .'lardan bölüyorum.
                date_list = date.split(".") #dışardan girdiğim tarihide aynı şekilde böldüm

                if (date_list[2] > expiration_date_list[2]): #Önce Yıla bakıyorum. Eğer girdiğim yıldan düşükse direk girip sil.
                         self.DeleteExpired(i[0])

                elif (date_list[2] == expiration_date_list[2] and date_list[1] > expiration_date_list[1] ): #Eğer yıllar eşitse aya bakıyorum. Girdiğim ay'dan düşükse girip sil
                    self.DeleteExpired(i[0])
                elif (date_list[2] == expiration_date_list[2] and date_list[1] == expiration_date_list[1] and date_list[0] > expiration_date_list[0]):
                    self.DeleteExpired(i[0])
    def Selling(self,name):
        self.sellname = name
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query,(name,))
        product = self.cursor.fetchall()

        if (len(product) == 0):
            print("No such product")

        else:
            if(self.firsLogin):
    #her seferinde self.product.stock=product[0][5] yaparsa aynı üründen birden çok satın alınca 1 tane düşürüyor. Bu yüzden buna sadece en başta 1 defa girmesi için if'e soktum.
                self.product_stock = product[0][5]
                self.product_stock -= 1

                self.totalPrice += product[0][2]   

                print("Product add to cart !")

                self.firsLogin= False  #Burda False yapıyorum ki birdaha girmesin. Taa ki fiş kesilene kadar. Her fiş kesiminde ürün stoğunu güncelleyecek.
                                   #Tekrardan satis yapılacağı zaman cutPlug metodunda True yaptığımız için tekrar satış yapacağımızda yine ilk defasında 1 defa giriyor if'e.
    def cutPlug(self):    
        query = "UPDATE products SET stock = ? WHERE name = ?"  #Burda güncellememin sebebi, Fis kesmeden ürünün stoktan düşmemesi için. 
        self.cursor.execute(query,(self.product_stock,self.sellname)) #Fişi kesiyoruz ve ürünü stoktan düşüyoruz.
        self.connect.commit()
        print("Total price : {}".format(self.totalPrice))
        self.dailyTotalCustomer +=1
        self.totalCiro += self.totalPrice

        self.firsLogin= True #fiş girildikten sonra tekrar true yapıyoruz
        self.totalPrice = 0

    def DailytotalCustomernumber(self):
        print("You have served a total of {} customers today".format(self.dailyTotalCustomer))

    def DailyCiroCalculate(self):

        if(self.totalCiro > 0):
            print("-"*10)
            print("Profit are")
        elif(self.totalCiro < 0):
            print("A loss here")
        print("Daily total ciro : {} TL".format(self.totalCiro))

    def getRefund(self,name):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query,(name,))
        products = self.cursor.fetchall()
        stock = products[0][5]
        stock += 1
        self.totalCiro -= products[0][2]
        query2 = "UPDATE products SET stock = ? WHERE name = ?"
        self.cursor.execute(query2,(stock,name))
        self.connect.commit()

        print("Returns Received ! Thanks")
        self.dailyTotalreturn += 1

    def DailygetRefunNumber(self):
        print("You have received total {} refunds today".format(self.dailyTotalreturn))
    
    def CloseSafe(self):
        connect2 = sqlite3.connect("dailydata.db")
        cursor2 = connect2.cursor()
        query = "CREATE TABLE IF NOT EXISTS dailydata(dailyTotalCustomer INT, dailyTotalciro INT , dailyTotalreturn INT )"
        cursor2.execute(query)
        connect2.commit()

        query = "INSERT INTO dailydata VALUES(?,?,?)"
        cursor2.execute(query,(self.dailyTotalCustomer,self.totalCiro,self.dailyTotalreturn))
        connect2.commit()

        self.dailyTotalCustomer =0
        self.totalCiro =0
        self.dailyTotalreturn =0