import requests
from bs4 import  BeautifulSoup

url = "https://www.n11.com/bilgisayar/masaustu-bilgisayar"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

listt = soup.find_all("li",{"class":"column"})

for product in listt:
    name = product.div.a.h3.text.strip()
    link = product.div.a.get("href")
    price = product.find("div",{"class":"proDetail"}).find("ins").text
    oldprice = product.find("div",{"class":"proDetail"}).find_all("a",{"class":"oldPrice"})[0].text.strip().strip("TL")
    print(F' name : {name} link = {link} old price : {oldprice} price :{price}')
