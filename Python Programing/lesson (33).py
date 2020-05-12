mylist = [1,2,3]
myString = 'my String'

class Movie():   
    def __init__(self,title,director,duration):
        self.title= title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu")
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __del__(self):
        return print(f" film silindi ")
    def __len__(self):
        return self.duration


m= Movie('filmin adı', 'yönetmen adı',120)
del m
print(type(m))

print(str(mylist))
print(str(m))

