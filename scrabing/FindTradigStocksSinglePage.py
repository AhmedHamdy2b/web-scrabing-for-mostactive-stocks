import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

symbols = [] 

result = requests.get("https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=9")
src = result.content

soup =BeautifulSoup(src,"lxml")

symbol = soup("td", {"class":"last col_symbol"})


for i in range(len(symbol)):
    symbols.append(symbol[i].text)
    
print("run scrape")

myfile = open('watchlist.csv', 'w')
for s in symbols:
	myfile.write(s + '\n')
myfile.close()