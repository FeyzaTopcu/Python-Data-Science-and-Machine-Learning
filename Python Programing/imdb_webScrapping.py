import requests 
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

listt = soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit =10)
 
for i in listt:
    title = i.find("td",{"class":"titleColumn"}).find("a").text
    year= i.find("td",{"class": "titleColumn"}).find("span").text
    rating = i.find("td",{"class":"ratingColumn"}).find("strong").text
    print(f'Film : {title.ljust(40)}  year : {year.strip("()")} rating : {rating}')