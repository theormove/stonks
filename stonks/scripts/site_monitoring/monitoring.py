from aljazeera import aj_gather_data
from reuters import re_gather_data
from economist import ec_gather_data
import django, sys, os


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
            	Post(title = post.title, content = post.text, source = post.source).save()
            posts = re_gather_data()
            for post in posts:
            	Post(title = post.title, content = post.text, source = post.source).save()
            posts = ec_gather_data()
            for post in posts:
            	Post(title = post.title, content = post.text, source = post.source).save()
            time.sleep(60)

        except ConnectionError:
            time.sleep(300)

check_for_updates()