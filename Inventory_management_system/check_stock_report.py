
# This file not will run from this location because it is module and all files manage from manage_shop.py

import json


def all_product_information(JSON_data):
    with open (JSON_data, "r") as file:
        
        data = json.load(file)
        print(f"Totle {len(data)} products are available")
        for student in data:
            print(student)
