from bs4 import  BeautifulSoup as bs
import requests

def scrape(url, method):

    session = requests.Session()
    response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = bs(response.content, 'html.parser', from_encoding='utf_8_sig')

    df = method(page)

    return df