# themoviedb.org => movie and series archive
# themoviedb list in your api application.
# Search by keyword
# Most popular movie list
# List of movies in the vision

import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "b86e788afdb2f8dd57ae3a4935152073"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def searchResult(self,keyword):
        self.keyword = keyword
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={self.keyword}&page=1")
        return response.json()

movie = theMovieDb()

while True:
    choise = input("1-Most Popular Movies\n2-Search Movies\n3-Exit\nCHOİSE:")
    
    if choise == '3':
        break
    elif choise == '1':
        result = movie.getPopulars()
        for moviee in result["results"]:
            print(moviee['title'])
    elif choise == '2':
        keyword = input("Enter the word you want to search:")   
        result = movie.searchResult(keyword)
        for keyword in result["results"]:
            print(keyword["name"])
        