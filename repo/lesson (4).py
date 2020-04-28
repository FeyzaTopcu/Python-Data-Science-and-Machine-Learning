dict 

person = {"name":"Feyza", "languages":["python","C#"]}

result = person["name"]
result = person["languages"][0]

import json 

#json string to Dict


person_json = '{"name":"Feyza", "languages":["python","C#"]}'


result = json.loads(person_json )

#result = result["name"]

result = result["languages"]

print(type(result))

print(result)


with open("person.json") as file:
    data = json.load(file)
    print(data)
    print(data["name"])
    print(data["languages"])

person_dict = {

    "name" : "Feyza",
    "languages": ["Python","C#"]

}


bilgi = {

    "kalem":"kağıt",
    "defter":"kitap",
}

detay = {

    "güzel":"günler",
    "her zaman":"seninle"
}
Dict to JSON string
result = json.dumps(person_dict)
print(type(result))

with open("person.json","a") as file :
    json.dump(person_dict,file) 

with open("person.json","a") as f:
    json.dump(bilgi,f)

with open("person.json","a") as g:
    json.dump(detay,g)
