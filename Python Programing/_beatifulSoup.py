html_doc = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Web Page</title>
</head>
<body>
    <div class="group1"> 
        <h1> Hello Everybody</h1>
        <ul> 
            <li> Menu 1</li>
            <li> Menu 2</li>
         </ul> 
        
        <h2> Python Lessons</h2>
        <ul> 
           <li> Menu 1</li>
           <li> Menu 2</li>
        </ul>

        <h2> C++ Lessons</h2>
        <ul> 
           <li> Menu 1</li>
           <li> Menu 2</li>
        </ul>

    </div>

    <div class="group2"> 
        <h1> Hello Everybody</h1>
        <ul> 
            <li> Menu 1</li>
            <li> Menu 2</li>
         </ul> 
        
        <h2> Python Lessons</h2>
        <ul> 
           <li> Menu 1</li>
           <li> Menu 2</li>
        </ul>

        <h2> C++ Lessons</h2>
        <ul> 
           <li> Menu 1</li>
           <li> Menu 2</li>
        </ul>

    </div>

    <div class="group3"> 
        <h1> Hello Everybody</h1>
        <ul> 
            <li> Menu 1</li>
            <li> Menu 2</li>
         </ul> 
        
        <h2> Python Lessons</h2>
        <ul> 
           <li> Menu 1</li>
           <li> Menu 2</li>
        </ul>

        <h2> C++ Lessons</h2>
        <ul> 
           <li> Menu 1</li>
           <li> Menu 2</li>
        </ul>

    </div>
    
     <img src="indir.jpeg" alt=""> 
     
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    <p> and they lived at the bottom of a well.</p>

</body>
</html>

"""

from bs4 import BeautifulSoup
soup =BeautifulSoup(html_doc,'html.parser')
result = soup.prettify()
result = soup.title
result = soup.body
result = soup.head
result = soup.title.name
result = soup.title.string  
result = soup.h1 
result = soup.h1.name
result = soup.h1.string

result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]

result = soup.div.ul.find_all('li')
result =soup.div.findChildren()

result = soup.div.findNextSibling().findNextSibling() 

result = soup.find_all('a')

for i in result:
    print(i.get('href'))

print(result)
