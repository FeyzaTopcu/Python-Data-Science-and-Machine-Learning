import requests
import json

impaired1 = input("impaired currency types:")
impaired2 = input("type of currency received:")
amount =int(input("how much currency do you want to exchange?:"))
api_url = "https://api.exchangeratesapi.io/latest?base="

result = requests.get(api_url+impaired1)

result = json.loads(result.text)

print("1 {0}: {1} {2}".format(impaired1,result["rates"][impaired2],impaired2))

print("{0} {1} = {2} {3}".format(amount,impaired1,amount * result["rates"][impaired2],impaired2))
