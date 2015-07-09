from settings import api_key, api_secret

from coinbase.client import Client

import requests
from time import sleep
import pprint


while True:
    data = requests.get('http://pubapi2.cryptsy.com/api.php?method=singlemarketdata&marketid=3').json()
    data = data['return']['markets']['LTC']
    label = data['label']
    price = data['lasttradeprice']
    time = data['lasttradetime']
    print '{}: {}'.format(label, price)
    sleep(5)



client = Client(api_key, api_secret)
wallet = client.get_account('')
print client.get_buy_price()
