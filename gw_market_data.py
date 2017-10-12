import requests
import json

price_url = 'https://api.guildwars2.com/v2/commerce/prices?ids='

def collect_material_prices(materials):
	material_ids = []
	for tier in materials.keys():
		for name in materials[tier].keys():
			material_ids.append(materials[tier][name]['id'])
	response_raw = requests.get(price_url + ','.join(material_ids))
	response = json.loads(response_raw.text)
	for tier in materials.keys():
		for name in materials[tier].keys():
			for material in response:
				if str(material['id']) == materials[tier][name]['id']:
					materials[tier][name]['buy_price'] = material['buys']['unit_price']
					materials[tier][name]['sell_price'] = material['sells']['unit_price']

def evaluate_profits(materials):
	for i in range(0, 5):
		current_tier = materials[str(i+1)]
		next_tier = materials[str(i+2)]
		print 'Tier ' + str(i+1) + ' -> Tier ' + str(i+2)
		for name in materials['1'].keys():
			dust_expense = int(next_tier['dust']['buy_price']) * 5
			current_tier_expense = int(current_tier[name]['buy_price']) * 50
			next_tier_expense = int(next_tier[name]['buy_price'])
			upgrade_cost = dust_expense + current_tier_expense + next_tier_expense
			upgrade_earnings = int(next_tier[name]['sell_price']) * 7
			profit = upgrade_earnings - upgrade_cost
			if profit > 0:
				print '  ' + name
				print '\tprofit: ' + str(profit)
				print '\tpurchase x50 ' + current_tier[name]['name'] + ' @ ' + str(current_tier[name]['buy_price'])
				print '\tpurchase x1 ' + next_tier[name]['name'] + ' @ ' + str(next_tier[name]['buy_price'])
				print '\tpurchase x5 ' + next_tier['dust']['name'] + ' @ ' + str(next_tier['dust']['buy_price'])
				print '\tsell x7 ' + next_tier[name]['name'] + ' @ ' + str(next_tier[name]['sell_price'])

materials_raw = open('json/materials.json').read()
materials = json.loads(materials_raw)
collect_material_prices(materials)
evaluate_profits(materials)
