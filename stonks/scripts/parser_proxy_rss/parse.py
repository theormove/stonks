import requests
from itertools import cycle
from bs4 import BeautifulSoup

def get_proxies():
    url = 'https://www.sslproxies.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features= "html.parser")
    print(response.text)
    proxies = []
    for i in soup.find('tbody').find_all('tr'):
        proxies.append(i.find('td').text)
    return proxies


#If you are copy pasting proxy ips, put in the list below
#proxies = ['121.129.127.206:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
with open('http_proxies.txt') as f:
    proxies = f.read().splitlines()

print(proxies)
proxy_pool = cycle(proxies)

url = 'http://icanhazip.com/'
for i in range(len(proxies)):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        request = requests.Session()
        request.proxies = {'http': proxy, 'https': proxy}
        response = request.get('https://www.pravda.com.ua/')

        print(response.text)
    except:
        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
        print("Skipping. Connnection error")