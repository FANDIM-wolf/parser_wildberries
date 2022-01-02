#gather data about clothes mango brand  and write down it in file


parse_url = "https://www.wildberries.ru/brands/mango/novaya-kollekciya"

class Product:
    
    def __init__(self,name,price):
        self.name = name 
        self.price = price 
    def get_name(self):
        return self.name

#contains objects 
list_of_prices_and_names = []        

from bs4 import BeautifulSoup
import requests as req

resp = req.get(parse_url)
list_of_prices_and_names = [] 
soup = BeautifulSoup(resp.text, 'lxml')
print(soup.prettify())
print("______")
counts = soup.find("span" , class_ ="goods-count")
cards  = soup.find_all("div" , class_="product-card-list")
brand_names = soup.find_all("div",class_="product-card__brand-name")
brand_prices = soup.find_all("span" , class_="lower-price")

print(counts.text)
print(brand_prices)
#create object and put it in list 
for brand_name in brand_names:
    for brand_price in brand_prices:
        print(brand_name.text  , " " , brand_price.text)
        object_from_card = Product(brand_name.text , brand_price.text)
        list_of_prices_and_names.append(object_from_card)
#put data in file 
with open('clothes_and_prices.txt' , 'w' , encoding='utf-8') as f:
    for item in list_of_prices_and_names :
        f.write("%s\n" % item)




