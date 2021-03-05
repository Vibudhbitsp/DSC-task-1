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
      with open(os.path.join('C:/Users/Asus/SUTT/images/cat1',book_name) ,'wb') as handler:
        
        handler.write(img_data)
f.close()
f2.close()