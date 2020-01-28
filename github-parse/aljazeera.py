import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
from article import Article
from scrape import scrape

path = "C:/Users/roman/PycharmProject/github-parse/aj/"


def aj_gather_data():

    global_url = 'https://www.aljazeera.com/news/'
    global_page= requests.get(global_url)
    global_soup = bs(global_page.text, features="html.parser")

    regions = global_soup.find('li', class_ = 'col-sm-4').find('ul').find_all('li')

    no_updates = True

    for region in regions[2:]:

        new_df = scrape('https://www.aljazeera.com' + region.find('a')['href'], aljazeera)
        updates = []
        file_name = "aj_" + str(region.find('a').text) + ".txt"

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

            if 'interactive.aljazeera' not in link:

                print("Aljazeera: new url in " + region.find('a').text + " region")

                index = int(new_df[new_df['link'] == link].index[0])
                title = new_df.loc[index, 'title']
                image = new_df.loc[index, 'image']

                text = ""
                tags = []

                session = requests.Session()
                response = session.get(link)
                soup = bs(response.content, 'html.parser', from_encoding='utf_8_sig')

                if soup.find('div', class_='article-body-tags') is not None:

                    text_all = soup.find('div', class_='article-p-wrapper').find_all('p')
                    tags_all = soup.find('div', class_='article-body-tags').find_all('li')

                    for t in text_all:
                        text += t.text

                    for tag in tags_all:
                        if tag is not None:
                            tags.append(tag.text)

                article = Article(title, link, image, text, tags, region.find('a').text)
                print(article)

    if no_updates:
        print("Aljazeera: no new urls")


def aljazeera(page):
    title, link, image = [], [], []

    df = pd.DataFrame()

    prefix = 'https://www.aljazeera.com'

    a = page.find_all('div', class_='frame-container')
    for i in a:
        title.append(i.find('img').get('title'))
        image.append(prefix + i.find('img').get('src'))
        temp = i.find('a').get('href')
        link.append(temp if 'www' in temp else (prefix + temp))

    b = page.find_all('div', class_='col-sm-7 topics-sec-item-cont')
    c = page.find_all('div', class_='col-sm-5 topics-sec-item-img')

    limit = max(len(b), len(c))
    j, k = max(limit - 1, 0), 0

    while j < limit:

        title.append(b[j].find('h2').text)
        temp = b[j].find_all('a')[1].get('href')
        link.append(temp if 'www' in temp else (prefix + temp))

        # when there is an opinion article
        # the image tag would change
        # terrible website
        if 'opinion' in b[j].find('a').get('href'):
            image.append(' ')

        else:
            image.append(prefix + c[k].find_all('img')[1].get('data-src'))
            k += 1

        j += 1

    df['title'] = title
    df['link'] = link
    df['image'] = image

    return df

