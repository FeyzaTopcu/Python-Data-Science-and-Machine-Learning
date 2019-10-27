with open('data2.txt','r') as my_file:
    with open('data2.txt','w') as my_file:
    print(my_file.read())
    my_file.seek(0)
    print(my_file.readline(8))
    print(my_file.tell())

    course= my_file.readlines()
    course = [ element.strip('\n') for element in course if '\n'  in element]

    print(course)

'''
    for course in my_file:
        print(my_file.readline())
'''
    