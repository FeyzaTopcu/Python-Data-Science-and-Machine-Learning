# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 08:48:16 2020

@author: FEYZA
"""

class Website:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name+" "+ self.surname)
        
        
class Website1(Website):
    def __init__(self,name,surname,id):
        Website.__init__(self,name,surname)
        self.id = id
        
    def Login(self):
        print(self.name+" "+ self.surname+" "+ self.id)
        
        

class Website2(Website):
    def __init__(self,name,surname,email):
        Website.__init__(self,name,surname)
        self.email = email
        
    def Login(self):
        print(self.name+" "+ self.surname+" "+ self.email)
        
        
w1 = Website("emin","topçu")

w2 = Website1("zeynep","topçu","1")

w3 = Website2("reyhan","topçu","deneme@")

w4 = Website1("şüheda","topçu","7")

w1.loginInfo()

w2.Login()
w3.Login()
w4.Login()
 