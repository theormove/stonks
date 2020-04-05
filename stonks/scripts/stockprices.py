
import django, sys, os, time

os.chdir("..")
sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
print(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] =  'stonks.settings'
django.setup()

from API.models import StockPrice

import requests 
import json
import requests
import bs4
import datetime 
from bs4 import BeautifulSoup

stockdata1 = {"Meta Data":{},
			"Time Series(5min)":{}}
			

def yahoo_graph(stockdataobj, link = "https://finance.yahoo.com/quote/RUB=X?p=RUB=X&.tsrc=fin-srch"):
	try:	
		r = requests.get(link)
		time = datetime.datetime.today()
		soup = BeautifulSoup(r.text, features="html.parser")
		value = soup.find_all("div", class_ = "My(6px) Pos(r) smartphone_Mt(6px)")[0].find('div').find('span').text 
		stockdataobj.data["Time Series(5min)"][str(time)] = {'open': value,
												'high': value,
												'low': value,
												'close': value,	
												'volume': '100',}
		print(stockdataobj.name)
		stockdataobj.save()
	except Exception as e:
				print(e.__doc__)	

def alpha_graph():
	with open('KEY.txt', 'r') as f:	
		key = f.read()
	try:
		msft = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey={}'.format(key))
		obj = StockPrice.objects.get(name='MSFT')
		obj.data = json.loads(msft.text)
		obj.save()
		print('Successfully added data to MSFT')
	except Exception as e:
		print(e.__doc__)

def run():
	while True:
		alpha_graph()
		yahoo_graph(StockPrice.objects.get(name='RUB/USD'))
		time.sleep(300)

run()			