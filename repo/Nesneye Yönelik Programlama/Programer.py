import time

class Programmer:
    def __init__(self,name,surname,language,project,amount):
        self.name = name
        self.surname = surname
        self.language = language
        self.project = project
        self.amount = amount

    def displayInformation(self):

        print("""
        Software name : {}
        Software surname : {}
        Software language : {}
        Software project : {}
        Software amount : {}
        """.format(self.name,self.surname,self.language,self.project,self.amount))

    def AddProject(self,newproject):
        
        print("Please waiting...")
        time.sleep(1)
        self.project.append(newproject)

        print(f" {newproject} add project list ")

    def AddLanguage(self,lang):


        self.language.append(lang)

        print(f" {lang} add language list")

    def Raise(self):
        amnt = int(input("Zam miktarını giriniz:"))
        self.amount += amnt
        print("Please waiting...")
        time.sleep(2)
        print(f"It was raise ")
        print(f"new amount :{self.amount}")

S1 = Programmer("feyza","topçu",["python,C"],["Speech Recognition"],3500)

S1.displayInformation()
#S1.Raise()
#S1.displayInformation()
S1.AddLanguage("Java")
S1.displayInformation()
S1.AddProject("Software Example")
S1.displayInformation()