import requests
import json

result = requests.get('https://jsonplaceholder.typicode.com/todos')

deger = json.loads(result.text)

print(deger)
print(type(deger))

print(deger[100]['title'])
print(deger[110])


for i in deger:
    if i["userId"] == 1:
        print(i["title"])
