    
# This file not will run from this location because it is module and all files manage from manage_shop.py

import os,json


def my_inventory(JSON_data,exiting_program):
    if not os.path.exists(JSON_data):
        print("Sorry! Database file does not exist.")
        exiting_program()        
        return
    
    with open (JSON_data, "r") as file:
        # this tri except for , when json file exists but empty then work it
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = [] 

        if len(data) == 0:
            print("No data found in the stock database.")
            exiting_program()
        else:
            for product in data:
                print(product)
            
            