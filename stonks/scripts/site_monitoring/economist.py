import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from site_monitoring.scrape import scrape
from site_monitoring.article import Article
import os

path = os.getcwd() + "/site_monitoring/ec/"


def ec_gather_data():

    global_url = 'https://www.economist.com/'
    global_page= requests.get(global_url)
    global_soup = bs(global_page.text, features="html.parser")

    regions = global_soup.find('ul', class_ ='ds-navigation-list-items--section').find_all('li')
    no_updates = True

    for region in regions[2:10]:
        new_df = scrape(region.find('a')['href'], economist)

        updates = []
        file_name = "ec_" + str(region.find('a').text) + ".txt"

        try:

            old_df = pd.read_pickle(os.path.join(path, file_name))

            for link in new_df['link'].tolist():

                if link not in old_df['link'].tolist():
                    updates.append(link)
                    no_updates = False

        except FileNotFoundError:
            pass

        open(os.path.join(path, file_name), "w", encoding='utf-8')
        new_df.to_pickle(os.path.join(path, file_name))

        for link in updates:

            print("Economist: new url in " + region.find('a').text + " region")

            index = int(new_df[new_df['link'] == link].index[0])
            title = new_df.loc[index, 'title']
            image = new_df.loc[index, 'image']

            text = ""
            tags = []

            session = requests.Session()
            response = session.get(link)
            soup = bs(response.content, 'html.parser', from_encoding='utf_8_sig')

            text_all = soup.find('div', class_='regwall__wrapper').find_all('p', class_='article__body-text')
            for t in text_all:
                text += t.text

            article = Article(title, link, image, text, tags, region.find('a').text)
            yield darticle

    if no_updates:
        print("Economist: no new urls")


def economist(page):
    title, link, image = [], [], []
    df = pd.DataFrame()
    prefix = 'https://www.economist.com'

    a = page.find_all('article', class_="teaser")

    for i in a:
        link.append(prefix + i.find('a').get('href'))
        title.append(i.find('span', class_='flytitle-and-title__title').text)
        image.append(i.parent.find('img').get('src'))

    df['title'] = title
    df['link'] = link
    df['image'] = image

    return df

ec_gather_data()
