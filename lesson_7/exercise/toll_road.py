import requests
from BeautifulSoup import BeautifulSoup
import time
import datetime
from functools import wraps
import csv

__author__ = 'sekely'

requests.packages.urllib3.disable_warnings()


def scheduled(period, delay=None, loop_count=None):
    delay = delay or 0
    loop_count = loop_count or 0

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            counter = 0
            time.sleep(delay)
            while True:
                start = time.time()
                if loop_count and loop_count > 0:
                    if counter == loop_count:
                        break
                    counter += 1
                func(*args, **kwargs)
                run_time = time.time() - start
                if run_time < period:
                    time.sleep(period - run_time)
        return wrapper
    return decorator


class TollRoad(object):
    _sample_rate = 5 * 60  # 5 min
    _csv_file = '/tmp/toll_road.csv'

    def __init__(self):
        self.create_csv_file()

    @staticmethod
    def get_price():
        r = requests.get('https://www.fastlane.co.il/mobile.aspx')
        parsed_html = BeautifulSoup(r.content)
        price = parsed_html.find('span', attrs={'id': 'lblPrice'}).text
        return int(price)

    @staticmethod
    def create_csv_file(f_name=_csv_file):
        with open(f_name, 'w') as f:
            headers = ['timestamp', 'price']
            writer = csv.DictWriter(f, headers)
            writer.writeheader()

    @staticmethod
    def save_to_csv(f_name=_csv_file, data=None):
        if not data:
            data = {'timestamp': str(datetime.datetime.now()),
                    'price': None}
        with open(f_name, 'a') as f:
            headers = ['timestamp', 'price']
            writer = csv.DictWriter(f, headers)
            writer.writerow(data)

    @scheduled(period=_sample_rate)
    def start_sampling(self):
        try:
            price = self.get_price()
        except:
            price = None
        data = {'timestamp': str(datetime.datetime.now()),
                'price': price}
        self.save_to_csv(data=data)

if __name__ == '__main__':
    tr = TollRoad()
    tr.start_sampling()
