import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/travel_2"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("travel.csv")
filename2 = ("bookname.csv")
f = open(filename,"w")
f2 = open(filename2,"w")
cat = "travel"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/travel/',book_name) ,'wb') as handler:
        
        handler.write(img_data)
f.close()





import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/mystery_3/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("mystery.csv")

f = open(filename,"w")

cat = "mystery"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/mystery/',book_name) ,'wb') as handler:
        
        handler.write(img_data)

url2 = "https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html"

r = requests.get(url2)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("mystery.csv")

f = open(filename,"w")

cat = "mystery"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist[0:10]:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/mystery/',book_name) ,'wb') as handler:
        
        handler.write(img_data)




import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("historicalfiction.csv")

f = open(filename,"w")

cat = "historicalfiction"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/historicalfiction/',book_name) ,'wb') as handler:
        
        handler.write(img_data)

url2 = "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-2.html"

r = requests.get(url2)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("historicalfiction.csv")

f = open(filename,"w")

cat = "historicalfiction"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/historicalfiction/',book_name) ,'wb') as handler:
        
        handler.write(img_data)




import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/parenting_28/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("parenting.csv")

f = open(filename,"w")

cat = "parenting"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/parenting/',book_name) ,'wb') as handler:
        
        handler.write(img_data)



import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/classics_6/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("classics.csv")

f = open(filename,"w")

cat = "classics"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/classics/',book_name) ,'wb') as handler:
        
        handler.write(img_data)

import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/sports-and-games_17/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("Sports and games.csv")

f = open(filename,"w")

cat = "sports and games"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/sports and games/',book_name) ,'wb') as handler:
        
        handler.write(img_data)





import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/suspense_44/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("suspense.csv")

f = open(filename,"w")

cat = "suspense"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/suspense/',book_name) ,'wb') as handler:
        handler.write(img_data)




import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/fiction_10/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("fiction.csv")

f = open(filename,"w")

cat = "fiction"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/fiction/',book_name) ,'wb') as handler:
        
        handler.write(img_data)

url2 = "https://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html"

r = requests.get(url2)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("fiction.csv")

f = open(filename,"w")

cat = "fiction"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist[0:10]:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/fiction/',book_name) ,'wb') as handler:
        
        handler.write(img_data)



import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/music_14/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("music.csv")

f = open(filename,"w")

cat = "music"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/music/',book_name) ,'wb') as handler:
        
        handler.write(img_data)




import os
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/category/books/new-adult_20/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
booklist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename = ("New adult.csv")

f = open(filename,"w")

cat = "New adult"
headers = "Book title,price,rating,availibility\n"
f.write(headers)
for books in booklist:
 
      book_title = books.h3.a["title"]
      book_price = books.find_all("p",{"class","price_color"})
      price = book_price[0].text.strip()
      book_rating = books.find_all("p",{"class","star-rating"})
      book_availability = books.find_all("p",{"class","instock availability"})
      f2.write(book_title + "," + cat + "\n")
      f.write(book_title + "," + str(price) + "," + str(book_rating[0]['class'][1]) + "," + str(book_availability[0].text.strip()) + "\n" ) 
      print("Title of the book :"+ book_title)
      print("rating of the book is",book_rating[0]['class'][1])
      print("Price of the book:", price)
      print("book is",book_availability[0].text.strip())
      img_url= books.find_all('img')
      print(url + img_url[0]['src'])
      img_data= requests.get(url + img_url[0]['src']).content
      book_name= book_title + '.jpg'
      with open(os.path.join('C:/Users/Asus/SUTT/images/New adult/',book_name) ,'wb') as handler:
        
        handler.write(img_data)