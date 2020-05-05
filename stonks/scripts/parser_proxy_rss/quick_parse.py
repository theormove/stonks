from bs4 import BeautifulSoup
import requests
import feedparser
import os
import random
import requests_random_user_agent


websites = []
from_one_ip = 10

forbidden = "/.:?.,=+& "

parse_dict = {'bbc':{'header':{'tag': "h1", 'class':"story-body__h1"}, 'paragraph':{'tag':"div", 'class':"story-body__inner"}},
              'cnbc': {'header':{'tag':"h1", 'class':"ArticleHeader-headline"}, 'paragraph':{'tag':"div", 'class':"group"}},
              'down_to_earth':{'header':{'tag':"h1", 'class':"detail-heading"}, 'paragraph':{'tag':"div", 'class':"news-detail-content"}},
              'economist':{'header':{'tag':"span", 'class':"article__headline"}, 'paragraph':{'tag':"tag", 'class':"class"}},
              'guardian':{'header':{'tag':"h1", 'class':"content__headline"}, 'paragraph':{'tag':"div", 'class':"content__article-body"}},
              'cnn':{'header':{'tag':"h1", 'class':"pg-headline"}, 'paragraph':{'tag':"div", 'class':"content__article-body"}},
              'wp':{'header':{'tag':"h1", 'class':"font--headline"}, 'paragraph':{'tag':"div", 'class':"remainder-content"}},
              'aj':{'header':{'tag':"h1", 'class':"post-title"}, 'paragraph':{'tag':"div", 'class':"main-article-body"}},
              'ch_d':{'header':{'tag':"h1", 'class':""}, 'paragraph':{'tag':"div", 'class':"main_art"}},
}

with open('http_proxies.txt') as https:
    proxies = https.read().splitlines()

for file in os.listdir('rss_links/'):
    websites.append(file.replace(".txt", ""))


def write_categories(link, name):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, features="html.parser")

    with open("rss_links/" + name + ".txt", "w") as f:

        all = soup.find('td', class_ = 'cnnBodyText').find_all(href = True)
        print(all)

        for l in all:
            f.write(l['href'])
            f.write("\n")


def make_filename(link):
    t_link = link
    for symbol in forbidden:
        t_link = t_link.replace(symbol, "")
    return t_link


def write_list_links():
    for site in websites[2:3]:
        path = "last_links/" + site + "/"
        print(path)
        f = open("rss_links/" + site + ".txt", "r")
        links = f.read().splitlines()

        for link in links:

            t_link = make_filename(link)

            name = path + t_link + ".txt"
            print(name)
            with open(name, "w+") as f_link:

                feed = feedparser.parse(link)
                for entry in feed.entries:
                    print(entry['link'])
                    #print(entry['title'])
                    f_link.write(entry['link'])
                    #f_link.write("\n" + entry['pubDate'])
                    f_link.write("\n")


def parse_article(link, website, requests_numb, proxy):

    parsed = False
    text = ""
    print("Parse_article, current proxy:")
    print(proxy)

    try:
        request = requests.Session()
        page = request.get(link)
        soup = BeautifulSoup(page.text, features="html.parser")

        try:
            if website != 'it':
                header = soup.find(parse_dict[website]['header']['tag'], class_=parse_dict[website]['header']['class']).text

                if website != 'cnn' and website != 'ch_d':
                    text_all = soup.find(parse_dict[website]['paragraph']['tag'],
                                     class_=parse_dict[website]['paragraph']['class']).find_all_next('p')
                elif website is 'cnn':
                    text_all = soup.find_all('div', class_='zn-body__paragraph')
                elif website is 'ch_d':
                    text_all = soup.find('div', {"id": 'Content'}).find_all('p')

                for p in text_all:
                    text += p.text + "\n"

                print(header)
                print(text)

            else:
                header = soup.find('title').text
                text += soup.find('div', class_ = "Normal").text

                print(header)
                print(text)

        except:
            requests_numb -=1
            return proxy

        parsed = True
        requests_numb -= 1

    except:

        if requests_numb is from_one_ip:
            requests_numb = 0
            proxy = random.choice(proxies)

            while not parsed:
                try:

                    request = requests.Session()
                    request.proxies = {'http': proxy, 'https': proxy}
                    print(request.proxies)
                    page = request.get(link)
                    soup = BeautifulSoup(page.text, features="html.parser")

                    if website != 'it':
                        header = soup.find(parse_dict[website]['header']['tag'],
                                           class_=parse_dict[website]['header']['class']).text

                        if website != 'cnn' and website != 'ch_d':
                            text_all = soup.find(parse_dict[website]['paragraph']['tag'],
                                                 class_=parse_dict[website]['paragraph']['class']).find_all_next('p')
                        elif website is 'cnn':
                            text_all = soup.find_all('div', class_='zn-body__paragraph')
                        elif website is 'ch_d':
                            text_all = soup.find('div', {"id": 'Content'}).find_all('p')

                        for p in text_all:
                            text += p.text + "\n"

                        print(header)
                        print(text)

                    else:
                        header = soup.find('title').text
                        text += soup.find('div', class_="Normal").text

                        print(header)
                        print(text)

                    parsed = True

                except:
                    proxy = random.choice(proxies)
                    print("Failure")
                    requests_numb = 0

    return proxy


def check_for_new_links():

    requests_number = 0

    proxy = random.choice(proxies)

    for site in websites:

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(site)

        path = "last_links/" + site + "/"

        f = open("rss_links/" + site + ".txt", "r")
        links = f.read().splitlines()
        for link in links:

            t_link = make_filename(link)
            name = path + t_link + ".txt"
            filee = open(name, "r")
            old_links = filee.read().splitlines()
            new_links = []
            i = 0

            for entry in feedparser.parse(link).entries:
                if entry['link'] not in old_links:
                    print(entry['link'])
                    proxy = parse_article(entry['link'], site, requests_number, proxy)
                    requests_number += 1
                    i+=1
                    new_links.append(entry['link'])

                else:
                    break

            with open(name, "w") as new_file:
                for link in new_links:
                    new_file.write(link + "\n")
                for link in old_links[0:len(old_links)-i]:
                    new_file.write(link + "\n")

#write_categories("https://edition.cnn.com/services/rss/", "cnn")
#write_list_links()

while True:
    check_for_new_links()