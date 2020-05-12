my_file = open('movies.txt', 'r')
print(my_file.name)
print(my_file.mode)

print(my_file.read())
my_file.close()
print("-----")
# content manager
with open('movies.txt', 'r') as my_file:

   print(my_file.read(5))
   
my_file.close()

print("-----")

# content manager
with open('movies.txt', 'r') as my_file:

    for line in my_file:
        print(line)
my_file.close()
print("-----")

# content manager
with open('movies.txt', 'r') as my_file:

    print(my_file.readline() ,end='')
    print(my_file.readline())
    print(my_file.readline())

my_file.close()

with open('data.txt','w') as my_file:

    my_file.write('Godzilla\n')
    my_file.write('The Room\n')
    print('Goliat', file=my_file)

my_file.close()

with open('data.txt', 'a') as my_file:
    my_file.write('Superman')
my_file.close()


with open('data2.txt', 'x') as my_file:
    my_file.write('Python \n')
    my_file.write('Django\n')
    my_file.write('Flask')