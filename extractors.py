import requests
from settings import coindelta_api, koinex_api, coinmarketcap_api

def data_collector():
    coin_data = {}
    coindelta = requests.get(coindelta_api)
    if coindelta.status_code == 200:
        coins = ['btc-inr', 'eth-inr', 'ltc-inr', 'omg-inr', 'qtum-inr', 'xrp-inr', 'bch-inr']
        for coin in coindelta.json():
            if coin['MarketName'] in coins:
                coin_data[coin['MarketName'].split('-')[0]] = {}
                coin_data[coin['MarketName'].split('-')[0]]['coindelta'] = {
                    'ask': float(coin['Ask']),
                    'bid': float(coin['Bid']),
                    'last': float(coin['Last'])
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

    coinmarketcap = requests.get(coinmarketcap_api)
    if coinmarketcap.status_code == 200:
        coins = ['BTC', 'ETH', 'LTC', 'XRP', 'BCH', 'QTUM', 'OMG']
        for coin in coins:
            for crypto in coinmarketcap.json():
                if crypto['symbol'] == coin:
                    coin_data[coin.lower()]['coinmarketcap'] = {
                        'last': round(float(crypto['price_inr']), 2)
                    }

    for coin in ['xrp', 'eth', 'ltc', 'btc', 'bch']:
        coin_data[coin]['diffco'] = round(coin_data[coin]['koinex']['bid']-coin_data[coin]['coindelta']['ask'], 2)
        coin_data[coin]['percco'] = round(((100/coin_data[coin]['coindelta']['ask'])*coin_data[coin]['koinex']['bid'])-100, 4)
        coin_data[coin]['diffko'] = round(coin_data[coin]['coindelta']['bid']-coin_data[coin]['koinex']['ask'], 2)
        coin_data[coin]['percko'] = round(((100/coin_data[coin]['koinex']['ask'])*coin_data[coin]['coindelta']['bid'])-100, 4)


    return coin_data
