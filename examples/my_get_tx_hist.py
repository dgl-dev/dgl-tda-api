import json
from urllib.request import urlopen

import atexit
import datetime
import dateutil
import sys
import tda

API_KEY = 'FON1HLNGRN0KOVR6UDTCF4RPEMPYIXOB@AMER.OAUTHAP'
REDIRECT_URI = 'http://localhost:8080/'
TOKEN_PATH = '../access_token'

def save_to_file(data):
    """
Save to file for testing
    """
    with open('../journal/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def make_webdriver():
    # Import selenium here because it's slow to import
    from selenium import webdriver

    driver = webdriver.Chrome()
    atexit.register(lambda: driver.quit())
    return driver


# Create a new client
client = tda.auth.easy_client(
    API_KEY,
    REDIRECT_URI,
    TOKEN_PATH,
    make_webdriver)

std = datetime.date(2021,8,1)
etd = datetime.date(2021,11,30)
tx_type = client.Transactions.TransactionType.TRADE

r = client.get_transactions(490673362,
                            transaction_type=tx_type,
                            start_date=std, end_date=etd)
#print(json.dumps(r.json()))
with open('../journal/data.json', 'w', encoding='utf-8') as f:

    for tx in r.json():
        json.dump(tx, f, ensure_ascii=False, indent=4)
#     print(json.dumps(tx, indent=1))
#     print("\n +++++++++++ \n")
#
# print(f'Keys of dict: {tx.keys()}')
# print(f"Keys of fees: {tx['fees'].keys()}")
# print(f"Keys of transactionItem: {tx['transactionItem'].keys()}")



