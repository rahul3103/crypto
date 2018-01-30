import time
import datetime
from huey import RedisHuey, crontab
from extractors import data_collector
from model import Crypto, db

huey = RedisHuey('jobs', host='localhost', port=6379)

@huey.periodic_task(crontab(minute='*/1'))
def request_coin_price():
    coin_prices = data_collector()
    with db.atomic():
        Crypto.insert_many(coin_prices).execute()
    print(coin_prices)
