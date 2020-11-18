#!/usr/bin/env python

import colorama
from colorama import Fore, Style

class MaterialEvaluator():
    def __init__(self, materials): 
        self.materials = materials

    def evaluate_and_output(self):
        """Evaluates and outputs projected profits for crafting materials"""
        for i in range(1, 6):
            current_tier = self.materials[str(i)]
            next_tier = self.materials[str(i+1)]
            print(Fore.RED + Style.BRIGHT + 'Tier ' + str(i) + ' -> Tier ' + str(i+1))
            for name in self.materials['1'].keys():
                current_tier_buy_price = current_tier[name]['buy_price']
                next_tier_buy_price = next_tier[name]['buy_price']
                next_tier_sell_price = next_tier[name]['sell_price']
                dust_expense = int(next_tier['dust']['buy_price']) * 5
                current_tier_expense = int(current_tier_buy_price + 1) * 50
                next_tier_expense = int(next_tier_buy_price + 1)
                upgrade_cost = dust_expense + current_tier_expense + next_tier_expense
                upgrade_earnings = int(next_tier_sell_price - 1) * 7
                profit = upgrade_earnings - upgrade_cost
                if profit > 0:
                    print(Fore.BLUE + Style.BRIGHT + '  ' + name)
                    print(Fore.GREEN + '\tprofit: ' + str(profit))
                    print(Fore.GREEN + '\tpurchase x50 ' + current_tier[name]['name'] + ' @ ' + str(current_tier_buy_price))
                    print(Fore.GREEN + '\tpurchase x1 ' + next_tier[name]['name'] + ' @ ' + str(next_tier_buy_price))
                    print(Fore.GREEN + '\tpurchase x5 ' + next_tier['dust']['name'] + ' @ ' + str(next_tier['dust']['buy_price']))
                    print(Fore.GREEN + '\tsell x7 ' + next_tier[name]['name'] + ' @ ' + str(next_tier_sell_price))
