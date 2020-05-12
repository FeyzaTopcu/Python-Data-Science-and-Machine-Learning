message = ' hello there. My name is Feyza'

message = message.upper()
print(message)
message = message.lower()
print(message)
message = message.title()
print(message)
message = message.capitalize()
print(message)
message = message.strip()
print(message)
message = message.split()
print(message)

message = '--'.join(message)
print(message)

index = message.find('feyza')
print(index)
k = message.startswith('l')
print(k)

message = message.replace('ç', 'c').replace('ş','s')
print(message)
message = message.center(50, '*')

print(message)


