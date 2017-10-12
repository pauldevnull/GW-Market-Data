"""Gathers and evaluates market data for GW2 crafting materials"""
#!/usr/bin/env python
import json
import requests

PRICE_URL = 'https://api.guildwars2.com/v2/commerce/prices?ids='

def collect_material_prices(materials):
    """Collects current crafting material prices"""
    material_ids = []
    for tier in materials.keys():
        for name in materials[tier].keys():
            material_ids.append(materials[tier][name]['id'])
    response_raw = requests.get(PRICE_URL + ','.join(material_ids))
    response = json.loads(response_raw.text)
    for tier in materials.keys():
        for name in materials[tier].keys():
            for material in response:
                if str(material['id']) == materials[tier][name]['id']:
                    materials[tier][name]['buy_price'] = material['buys']['unit_price']
                    materials[tier][name]['sell_price'] = material['sells']['unit_price']

def evaluate_material_profits(materials):
    """Evaluates and outputs projected profits for crafting materials"""
    for i in range(1, 6):
        current_tier = materials[str(i)]
        next_tier = materials[str(i+1)]
        print 'Tier ' + str(i) + ' -> Tier ' + str(i+1)
        for name in materials['1'].keys():
            current_tier_buy_price = current_tier[name]['buy_price']
            next_tier_buy_price = next_tier[name]['buy_price']
            next_tier_sell_price = next_tier[name]['sell_price']
            dust_expense = int(next_tier['dust']['buy_price']) * 5
            current_tier_expense = int(current_tier_buy_price) * 50
            next_tier_expense = int(next_tier_buy_price)
            upgrade_cost = dust_expense + current_tier_expense + next_tier_expense
            upgrade_earnings = int(next_tier_sell_price) * 7
            profit = upgrade_earnings - upgrade_cost
            if profit > 0:
                print '  ' + name
                print '\tprofit: ' + str(profit)
                print '\tpurchase x50 ' + current_tier[name]['name'] + \
                    ' @ ' + str(current_tier_buy_price)
                print '\tpurchase x1 ' + next_tier[name]['name'] + \
                    ' @ ' + str(next_tier_buy_price)
                print '\tpurchase x5 ' + next_tier['dust']['name'] + \
                    ' @ ' + str(next_tier['dust']['buy_price'])
                print '\tsell x7 ' + next_tier[name]['name'] + \
                    ' @ ' + str(next_tier_sell_price)

MATERIALS_RAW = open('json/materials.json').read()
MATERIALS = json.loads(MATERIALS_RAW)
collect_material_prices(MATERIALS)
evaluate_material_profits(MATERIALS)
