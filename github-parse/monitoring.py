from aljazeera import aj_gather_data
from reuters import re_gather_data
from economist import ec_gather_data
import time

def check_for_updates():

    while True:
        try:
            aj_gather_data()
            re_gather_data()
            ec_gather_data()
            time.sleep(60)

        except ConnectionError:
            time.sleep(300)

check_for_updates()