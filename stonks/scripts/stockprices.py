
import django, sys, os, time

os.chdir("..")
sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
print(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] =  'stonks.settings'
django.setup()

from API.models import StockPrice

import requests 
import json

with open('KEY.txt', 'r') as f:
	key = f.read()
while True:
	try:
		msft = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey={}'.format(key))
		obj = StockPrice.objects.get(name='MSFT')
		obj.data = msft.text
		obj.save()
		print('Successfully added data to MSFT')
	except Exception as e:
		print(e.__doc__)
		print(e.message)
	time.sleep(300)	