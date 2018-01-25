import json
from flask import Flask, jsonify, request, render_template
# from playhouse.shortcuts import model_to_dict
from flask_cors import CORS
# from model import Crypto
# from peewee import create_model_tables
from extractors import data_collector

app = Flask(__name__)
CORS(app)

# create_model_tables([Crypto], fail_silently=True)

# @app.route('/api/crypto/<coin>/<period>', methods=['GET'])
# def users(coin, period):
#     if request.method == 'GET':
#         coins = Crypto.select().where(Crypto.coin == coin).order_by(Crypto.cdate.desc())
#         if coins:
#             if period == 'past':
#                 return (jsonify(coins=[coin.to_dict([Crypto.id, Crypto.coin]) for coin in coins])), 200
#             if period == 'current':
#                 coins =  coin_price()
#                 for ccoin in coins:
#                     if ccoin['name'] == coin:
#                         return jsonify({ coin: ccoin['value']}), 200
#
#         return json.dumps({'Error': coin + ' Cryptocoin not added yet or period is not corrrect'}), 400

@app.route('/')
def index():
    data = data_collector()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
