import requests
from bs4 import BeautifulSoup

url = ["https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=1",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=2",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=3",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=4",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=5",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=6",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=7",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=8",
       "https://markets.financialcontent.com/stocks/stocks/dashboard/mostactive?CurrentPage=9"]

syms = []

for i in range(len(url)):
    result = requests.get(url[i])
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    symbol = soup("td", {"class":"last col_symbol"})

    for ia in range(len(symbol)):
        syms.append(symbol[ia].text)

    myfile = open('watchlist.csv', 'w')
    for s in syms:
        myfile.write(s + '\n')
    myfile.close()
