
# This file not will run from this location because it is module and all files manage from manage_shop.py


import os,json
# JSON_data = r"S:\python_project(inventory_management_system)\Indixpert-FSD-April-Python-Pr04\stock.json"


def single_product_information(JSON_data, exiting_program):
    if not os.path.exists(JSON_data):
        print("Sorry! Database file does not exist.")
        exiting_program()        
        return
    with open (JSON_data, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = [] 

        if len(data) == 0:
            print("No data found in the stock database.")
            exiting_program()
        else:
            product_name = input("Enter the product name: ").strip()

            for product in data:
                if product["product"]["name"]==product_name:
                    print(f"product found: \n{product}")
                    exiting_program()


