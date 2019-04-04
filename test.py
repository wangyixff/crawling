import pandas as pd
import requests
from requests import get
import urllib.request

from downloadHTML import download


htmlstring = download('https://www.sportchek.ca/services/sportchek/search-and-promote/products?q=sweater+women&lastVisibleProductNumber=1&page=1&count=1')
itemcount = json.loads(htmlstring)["resultCount"]["total"]
htmlstring = download('https://www.sportchek.ca/services/sportchek/search-and-promote/products?q=sweater+women&lastVisibleProductNumber=1&page=1&count=' + str(itemcount))

with open("sportschek.html", "w") as file:
    file.write(htmlstring)

temp = json.loads(htmlstring)
products = temp["products"]
df = pd.DataFrame()

title = [] #string
brand = [] #string
availability = [] #string
clearancePrice = [] #boolean
features = [] #ul list strings
imageAndColor = [] #list
inStock = [] # boolean
longDescription = [] #string
onlineOnly = [] #boolean
price = [] #float
priceData = [] #string
rating = [] #number

for product in products:
    title.append(product["title"])
    brand.append(product["brand"])
    availability.append(product["availability"])
    clearancePrice.append(product["clearancePrice"])
    features.append(product["features"])
    imageAndColor.append(product["imageAndColor"])
    inStock.append(product["inStock"])
    longDescription.append(product["longDescription"])
    onlineOnly.append(product["onlineOnly"])
    price.append(product["price"])
    priceData.append(product["priceData"])
    rating.append(product["rating"])

df['title'] = title
df['brand'] = brand
df['availability'] = availability
df['clearancePrice'] = clearancePrice
df['features'] = features
df['imageAndColor'] = imageAndColor
df['inStock']= inStock
df['longDescription'] = longDescription
df['onlineOnly'] = onlineOnly
df['price'] = price
df['priceData'] = priceData
df['rating'] = rating

df.head()
#or you can convert the whole list to dataframe directly
df2 = pd.DataFrame(products)
df2.head()



