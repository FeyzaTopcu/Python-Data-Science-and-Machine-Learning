import re
result = dir(re)

print(result)

#re module
strr = "Python çalışma günlüğünde Python dersleri 90"

#re.findall()

result = re.findall("çalışma",strr)

result= len(result)

result = re.split("a",strr)


re.sub()

result= re.sub(" ","-",strr)
result = re.sub("\s", "-",strr)


re.search()

result = re.search("Python",strr)

result = result.span() #match objesinin konumu

result = result.end()

result = result.start()

result = result.group()

result = result.string

print(result)

regular expression 

result = re.findall("[abc]",strr)

result = re.findall("[sat]",strr)

result = result.findall("[a-z]",strr)

result =  result.findall("[1-5]",strr)

result = re.findall("...",strr)

result = re.findall("Py..on",strr)

result = re.findall("^çalışma",strr)

result  = re.findall("i$",strr)
result = re.findall("t$",strr)

result = re.findall("ça*l",strr)

result = re.findall("ça+l",strr)

result = re.findall("\APython",strr)

result = re.findall("90\D",strr)
print(result)