import json
from string import Template

import requests

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def insert_coins():
    # Get data
    data_requests = requests.get(
        "https://min-api.cryptocompare.com/data/all/coinlist"
    )
    data = json.loads(data_requests.content)

    for item in data['Data'].values():
        totalCoinSupply=item.get('TotalCoinSupply', 0.0)
        if totalCoinSupply == 'N/A':
            totalCoinSupply = 0.00
        else:
            totalCoinSupply = strip_non_ascii(totalCoinSupply)
            totalCoinSupply = totalCoinSupply.replace(' ', '')
            totalCoinSupply = totalCoinSupply.replace(',', '')
            dots = totalCoinSupply.count('.')
            if dots > 1:
                totalCoinSupply = totalCoinSupply.replace('.', '', dots - 1)
            totalCoinSupply = round(float(totalCoinSupply), 2)

        totalCoinsMined = item.get('totalCoinsMined', 0.0)
        totalCoinsMined = round(float(totalCoinsMined), 8)

        netHashesPerSecond = item.get('NetHashesPerSecond', 0.0)
        netHashesPerSecond = round(float(netHashesPerSecond), 8)

        blockReward = item.get('BlockReward', 0.0)
        blockReward = round(float(blockReward), 8)

        blockTime = item.get('BlockTime', -1)

        blockNumber = item.get('BlockNumber', -1)

        imageUrl = item.get('ImageUrl', '')

        payload = {}
        payload['imageUrl'] = imageUrl
        payload['name'] = item['CoinName']
        payload['symbol'] = item['Symbol']
        payload['algorithm'] = item['Algorithm']
        payload['proofType'] = item['ProofType']
        payload['totalCoinSupply'] = totalCoinSupply
        payload['isTrading'] = item['IsTrading']
        payload['totalCoinsMined'] = totalCoinsMined
        payload['blockNumber'] = blockNumber
        payload['netHashesPerSecond'] = netHashesPerSecond
        payload['blockReward'] = blockReward
        payload['blockTime'] = blockTime

        r = requests.post(
            'http://localhost:8000/api/coins/',
            data=payload
        )
        if r.status_code == 201:
            print(item['Id'], item['Name'], r.status_code)
        else:
            print('SOMETHING WENT WRONG ON THIS COIN', item['Id'])
            print(payload)

insert_coins()
