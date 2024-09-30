# This file not will run from this location because it is module and all files manage from manage_shop.py

import os,json


def all_product_information(JSON_data,exiting_program):
    if not os.path.exists(JSON_data):
        print("Sorry! Database file does not exist.")
        exiting_program()        
        return
    
    with open (JSON_data, "r") as file:
        # this tri except for , when json file exists but empty then work it
        try:
            list_data = json.load(file)
        except json.JSONDecodeError:
            list_data = [] 

        if len(list_data) == 0:
            print("No data found in the stock database.")
            exiting_program()
        else:
            
            product_name = input("Enter the product name: ").strip().lower()

            for product in list_data:
                if product["product"]["name"]==product_name:
                    print(f"{product["product"]["quantity"]} Units of {product_name} are left in your stock. Which id {product["product_id"]}")
                    exiting_program()
                
            # print(f"Product Error: This product is not available in your stock")