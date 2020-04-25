from supermarket import *
import time
productObj = SuperMarket()

print("""************************
Welcome in the SuperMarket App!
1. ADD PRODUCT
2. DELETE PRODUCT
3. STOCK INQUIRY (By Product Name):
4. INVENTORY INQUIRY (By Brand Name):
5. SUPERMARKET TOTAL PRODUCT STOCK INQUIRY
----------------------------------------
6. REMOVE EXPIRED DATES
----------------------------------------
7. SELL
8. REFUND
----------------------------------------
9. DAILY TOTAL NUMBER OF CUSTOMERS
10TH DAILY TOTAL REFUND NUMBER
11.DAY CALCULATE TURNOVER
----------------------------------------
12.Close Safe
************************ """)

while True:
    entry =input("Make a choice : ")
    if (entry =="12"):
        print("---------------")
        print("Safe Closed !")
        print("Program Ending...")
        productObj.CloseSafe()
        productObj.DisconnectDatabase()
        break
    elif (entry == "1"):

        poduct_name = input("Product name : ")
        brand = input ("Brand:")
        price = float (input ("Price:"))
        expiration_date=input ("Expiration Date:")
        product_Count = input ("Product Type:")
        stock=int(input("Stock : "))
        print("Added product...")
        time.sleep(1)
        productss=Product(poduct_name,brand,price,expiration_date,product_Count,stock)
        
        productObj.Add_Product(productss)   #fonksiyonları kullanmak için tek bir SuperMarket class nesnesi oluşturmak yeterli.
                                  #Add_Product fonksiyonunu kullanmak için her seferinde SuperMarket classı için nesne tanımlamaya gerek yok
                                  #Bu yüzden en başta urunNesne diye tanımlamamız yeterli.

        print("Added product...")

    elif (entry == "2"):
        productName = input ("Enter the Product Name You Want to Delete:")
        productObj.Delete_Product(productName)
    elif  (entry == "3"):
        productName = input("Enter the product name you want to query:")
        productObj.NameofqueryStock(productName)
    elif (entry == "4"):
        bland = input("Enter the Brand name you want to query:")
        productObj.BrandofqueryStock(bland)
    elif (entry=="5"):
        productObj.TotalProductStock()
    elif (entry=="6"):
        girdi = input("What Date Do You Want To Delete Before (Ex: 01.01.2018):")
        productObj.DeleteExpired(entry)
    elif (entry == "7"):
        while True:
            entry=input("Enter Product Name (cancel: i | voucher: f):")
            if (input == "i"):
                productObj.firsLogin = True  #Sepeti iptal edersek, cutPlug() teki gibi yine firstLogin'i True yapıyoruz ki birdahaki müşteride ilk defa stoğu alacağı if'e girebilsin.
                break
            elif(entry == "f"):
                print ("Receiving Voucher. Thanks for the payment!")
                productObj.cutPlug()
                break
            else:
                productObj.Selling(entry)
    elif (entry == "8"):
        entry = input("Enter the name of the product you want to return:")
        productObj.getRefund(entry)
    elif (entry == "9"):
        productObj.DailytotalCustomernumber()
    elif (entry == "11"):
        productObj.DailyCiroCalculate()
    else:
        print("Invalid transaction !")
    








      