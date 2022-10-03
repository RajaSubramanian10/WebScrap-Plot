# Scrap data from Flipkart for Redmi Mobile Phones

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url = "https://www.flipkart.com/search?q=redmi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
  p = requests.get(url)
  soup = BeautifulSoup(p.content,'html.parser')
  print(p)
content = soup.find_all('div', class_="_2kHMtA")
fheader = ["Product Name","Price","Original Price","Discount"]

itemfull = []

for item in content:
  items = []
  productname = item.find('div', class_="_4rR01T")
  price = item.find('div', class_="_30jeq3 _1_WHN1")
  original = item.find('div', class_="_3I9_wc _27UcVY")
  discount = item.find('div', class_="_3Ay6Sb")
  items.append(productname.text)
  if(price is not None):
    items.append(price.text)
  else:
    items.append("Price is NA")
  if(original is not None):
    items.append(original.text)
  else:
    items.append("No Original Price")
  if(discount is not None):
    items.append(discount.text)
  else:
    items.append("No Discount")
  itemfull.append(items)

pd.DataFrame(itemfull).to_csv("flipred.csv",header=fheader)
