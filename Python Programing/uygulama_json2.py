class User():
    def __init__(self,username,password,email):
        self.username = username,
        self.password =password,
        self.email = email

import json
import os

class UserRepository():
    def __init__(self):
        self.users = []
        self.isLogedIn = False,
        self.currentUser = {}

        #load users from .json file

        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('user2.json'):
            with open('user2.json','r',encoding= 'utf-8') as file:
                users = json.load(file)
                print(users)

    def register(self,user2 = User):
        self.users.append(user2)
        self.savetoFile()
        print('Kullanıcı oluşturuldu')

    
    def login(self):
        pass

    def savetoFile(self):
        liste = []

        for user in self.users:
            liste.append(json.dumps(user.__dict__))

        with open('user2.json','w') as file:
            json.dump(liste,file)


repository = UserRepository()

while True:
    print('MENÜ'.center(200,'*'))
    secim = input('1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\n seçiminiz :')
    if secim == '5':
        break
    else:
        if secim == '1':
            #register
            username = input('username:')
            password = input("password:")
            email = input("email:")

            user = User(username=username,password=password,email=email)
            repository.register(user)
            print(repository.users)

        elif secim == '2':
            #login
            pass
        elif secim == '3':
            #logout
            pass
        elif secim == '4':
            #display username
            pass
        else:
            print('yanlış seçim')

