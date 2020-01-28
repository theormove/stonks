import sys 
import os 
import django



sys.path.insert(0, '/home/me/stonks/stonks')
os.environ['DJANGO_SETTINGS_MODULE']= 'stonks.settings'
django.setup()

from news.models import Post
from scripts.news_monitoring.aljazeera import aj_gather_data
from scripts.news_monitoring.reuters import re_gather_data
from  scripts.news_monitoring.economist import ec_gather_data
import time



def check_for_updates():

    while True:
        try:
            new_post_aj = aj_gather_data()
            for post in new_post_aj:
                new_post = Post( title = post.title, content = post.text, source = post.link)
                new_post.save()
            new_post_re = re_gather_data()
            for post in new_post_re:
                new_post = Post( title = post.title, content = post.text, source = post.link)
                new_post.save()
            new_post_ec = ec_gather_data()  
            for post in new_post_ec:
                new_post = Post( title = post.title, content = post.text, source = post.link)
                new_post.save()
            time.sleep(60)

        except ConnectionError:
            time.sleep(300)

check_for_updates()

