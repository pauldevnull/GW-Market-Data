#!/usr/bin/env python

import json
from material_collector.material_collector import MaterialCollector
from material_evaluator.material_evaluator import MaterialEvaluator

def main():
    materials_raw = open('json/materials.json').read()
    materials = json.loads(materials_raw)

    material_collector = MaterialCollector(materials)
    material_evaluator = MaterialEvaluator(materials)

    material_collector.collect_material_prices()
    material_evaluator.evaluate_and_output()

main();
