import requests
import json 

class Github :
    def __init__(self):
        self.api = 'https://api.github.com'
        self.token = 'c538228f882d1778e4192d0b88823fd321e199d0'
    
    def getUser(self,username):
        response = requests.get(self.api +'/users/'+ username)
        return response.json( )         

    def getRepositories(self,username):
        response = requests.get(self.api+'/users/'+username+'/repos')
        return response.json()
    def createRepository(self, name):
        response = requests.post(self.api+'/user/repos?access_token='+ self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://feyzatopcu.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
    
    def deleteRepository(self,reponame,owner):
        self.reponame = reponame
        self.owner = owner
 
        response = requests.delete(self.api+'users/repos/:'+self.owner+'/:'+self.reponame,json={
            "name": reponame,
            "description": "This is your first repository",
            "homepage": "https://feyzatopcu.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })  
        return response.json()
    
        
github = Github()

while True: 
    choise = input('1-Find User\n2-Get Repositories\n3-Crate Repository\n4-Deleting Repository\n5-Exit\nChoise:')
   
    if choise == '5':
        break
    else:
        if choise == '1':
            username = input("Please writting username:")
            result = github.getUser(username)
            print(f"name : {result['name']} \npublic repos : {result['public_repos']} \nfollower : {result['followers']}")

        elif choise == '2':
            username = input("Please writting username:")
            result = github.getRepositories(username)
            
            for i in result:
                print(i['name'])
            
        elif choise == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result) 
            
        elif choise == '4':
            owner= input("Please type the person whose store you want to delete:")
            reponame = input("Please type the repo name you want to delete:")
            result = github.deleteRepository(reponame,owner)
            print(result)
            
            
        else:
            print("Wrong Choise")