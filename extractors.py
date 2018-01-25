import requests
from settings import coindelta_api, koinex_api

def data_collector():
    coin_data = {}
    coindelta = requests.get(coindelta_api)
    if coindelta.status_code == 200:
        coins = ['btc-inr', 'eth-inr', 'ltc-inr', 'omg-inr', 'qtum-inr', 'xrp-inr', 'bch-inr']
        for coin in coindelta.json():
            if coin['MarketName'] in coins:
                coin_data[coin['MarketName'].split('-')[0]] = {}
                coin_data[coin['MarketName'].split('-')[0]]['coindelta'] = {
                    'ask': coin['Ask'],
                    'bid': coin['Bid'],
                    'last': coin['Last']
                }

    koinex = requests.get(koinex_api)
    if koinex.status_code == 200:
        coins = ['BTC', 'ETH', 'LTC', 'XRP', 'BCH']
        for coin in coins:
            coin_data[coin.lower()]['koinex'] = {
                'ask': float(koinex.json()['stats'][coin]['lowest_ask']),
                'bid': float(koinex.json()['stats'][coin]['highest_bid']),
                'last': float(koinex.json()['stats'][coin]['last_traded_price'])
            }

    return coin_data
