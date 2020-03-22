from site_monitoring.aljazeera import aj_gather_data
from site_monitoring.reuters import re_gather_data
from site_monitoring.economist import ec_gather_data
from categorizer import categorizer
import django, sys, os, time

os.chdir("..")
sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
print(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] =  'stonks.settings'
django.setup()

from news.models import Post

def check_for_updates():

    while True:	
        try:
            posts = aj_gather_data()
            for post in posts:
            	Post(title = post.title, content = post.text, source = post.link, category = categorizer(post.text)).save()
            posts = re_gather_data()
            for post in posts:
            	Post(title = post.title, content = post.text, source = post.link, category = categorizer(post.text)).save()
            posts = ec_gather_data()
            for post in posts:
            	Post(title = post.title, content = post.text, source = post.link, category = categorizer(post.text)).save()
            time.sleep(60)

        except ConnectionError:
            time.sleep(300)

check_for_updates()