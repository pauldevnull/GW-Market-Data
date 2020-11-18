#!/usr/bin/env python

import json
import requests

class MaterialCollector():
    def __init__(self, materials): 
        self.materials = materials
        self.price_url = 'https://api.guildwars2.com/v2/commerce/prices?ids='

    def __collect_material_ids(self):
        """Collects crafting material identifiers"""
        material_ids = []
        for tier in self.materials.keys():
            for name in self.materials[tier].keys():
                material_ids.append(self.materials[tier][name]['id'])
        return material_ids

    def collect_material_prices(self):
        """Collects current crafting material prices"""
        material_ids = self.__collect_material_ids()
        response_raw = requests.get(self.price_url + ','.join(material_ids))
        response = json.loads(response_raw.text)
        for tier in self.materials.keys():
            for name in self.materials[tier].keys():
                for material in response:
                    if str(material['id']) == self.materials[tier][name]['id']:
                        self.materials[tier][name]['buy_price'] = material['buys']['unit_price']
                        self.materials[tier][name]['sell_price'] = material['sells']['unit_price']
