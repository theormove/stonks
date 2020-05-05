import feedparser
from bs4 import BeautifulSoup
import  requests
import requests_random_user_agent
from quick_parse import parse_dict


website = 'cnn'
text = ""
url = "http://rss.cnn.com/~r/rss/edition_us/~3/fvQDtUooGxs/index.html"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

header = soup.find(parse_dict[website]['header']['tag'], class_=parse_dict[website]['header']['class']).text
#text_all = soup.find(parse_dict[website]['paragraph']['tag'],
                                     #class_=parse_dict[website]['paragraph']['class']).find_all_next('p')
text_all = soup.find_all('div', class_='zn-body__paragraph')


for p in text_all:
    text += p.text + "\n"


print(header)
print(text)
'''
with open("rss_links/it.txt", "w+") as f:
    for ul in soup.find_all('ul', class_ = 'rssList'):
        links = ul.find_all(href = True)
        for link in links:
            f.write("https://economictimes.indiatimes.com" + link['href'])
            f.write('\n')
for i in range(10):
    s = requests.Session()
    print(s.headers)

response = requests.get("https://www.theguardian.com/world/2020/mar/29/britons-on-virus-hit-ship-wait-for-panama-canal-green-light")
soup = BeautifulSoup(response.text, features= "html.parser")

for p in soup.find('div', class_ = 'content__article-body').find_all('p'):
    print(p.text + "\n")

feed = feedparser.parse("https://www.downtoearth.org.in/rss/all")

for entry in feed.entries:
    print(entry['title'])
'''