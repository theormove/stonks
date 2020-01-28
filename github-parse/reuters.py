import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from scrape import scrape
from article import Article
import os

path = "C:/Users/roman/PycharmProject/github-parse/re/"


def re_gather_data():

    global_url = 'https://www.reuters.com/'
    global_page= requests.get(global_url)
    global_soup = bs(global_page.text, features="html.parser")

    regions = global_soup.find(id='nav-item-4').find('div', class_ ='subnav-inset').find_all('ul', class_= 'subnav-list')

    usa = True

    no_updates = True

    for regions_part in regions:

        if usa:
            usa = False
            regions_part_t = regions_part.find_all('li')[1:2]

        else:
            regions_part_t = regions_part.find_all('li')

        for region in regions_part_t:

            new_df = scrape('https://www.reuters.com' + region.find('a')['href'], reuters)
            updates = []
            file_name = "re_" + str(region.find('a').text) + ".txt"

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

                print("Reuters: new url in " + region.find('a').text + " region")

                index = int(new_df[new_df['link'] == link].index[0])
                title = new_df.loc[index, 'title']
                image = new_df.loc[index, 'image']

                text = ""
                tags = []

                session = requests.Session()
                response = session.get(link)
                soup = bs(response.content, 'html.parser', from_encoding='utf_8_sig')

                text_all = soup.find('div', class_='StandardArticleBody_body').find_all('p')

                for t in text_all:
                    text += t.text

                article = Article(title, link, image, text, tags, region.find('a').text)
                print(article)

    if no_updates:
        print("Reuters: no new urls")


def reuters(page):

    title, link, image = [], [], []
    df = pd.DataFrame()

    for p in page.find_all('div', class_='FeedItem_item'):

        t = p.find('h2').find('a').text
        title.append(t)

        l = p.find('h2').find('a')['href']
        link.append(l)

        try:
            if p.find('img') is not None:
                i = p.find('img')['src']
                image.append(i)
            else:
                image.append("")
        except KeyError:
            image.append("")

    df['title'] = title
    df['link'] = link
    df['image'] = image

    return df

re_gather_data()


