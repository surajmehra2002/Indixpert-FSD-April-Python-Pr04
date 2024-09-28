
# This file not will run from this location because it is module and all files manage from manage_shop.py

import json, os
from datetime import datetime


def add_product_in_stock(JSON_data):
    class Inventory:

        def add_product(self, id, name, price, quantity):
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            dict_format_item = {
                "name": name,
                "price": price,
                "quantity": quantity,
                "added_on": current_datetime  
            }
            new_product = {"product_id": id, "product": dict_format_item}

            if os.path.exists(JSON_data):
                with open(JSON_data, "r") as file:
                    try:
                        list_data = json.loads(file.read())
                    except json.JSONDecodeError:
                        list_data = []
            else:
                list_data = []

            list_data.append(new_product)

            list_data = sorted(list_data, key=lambda x: x["product_id"])

            with open(JSON_data, "w") as file:
                json_data = json.dumps(list_data, indent=None, separators=(",", ":"))  
                compact_json_data = json_data.replace("},", "}, \n")  
                compact_json_data1 = compact_json_data.replace('[', '[ \n')  
                compact_json_data2 = compact_json_data1.replace(']', '\n ]') 
                compact_json_data3 = compact_json_data2.replace(',"product":', ',\n "product":')  
                compact_json_data4 = compact_json_data3.replace('}}, ', '}}, \n') 
                file.write(compact_json_data4)
            print("Product added successfully to your stock.")

    stock = Inventory()

    while True:
        product_id = int(input("Enter Product ID: "))

        if os.path.exists(JSON_data):
            with open(JSON_data, "r") as file:
                try:
                    list_data = json.loads(file.read())
                except json.JSONDecodeError:
                    list_data = []
        else:
            list_data = []

        product_exists = any(product["product_id"] == product_id for product in list_data)

        if product_exists:
            print(f"Error: Product ID {product_id} already exists. Please enter a different product ID.")
        else:
            while True:
                product_name = input("Enter Product Name: ")
                product_name_exists = any(product["product"]["name"].lower() == product_name.lower() for product in list_data)

                if product_name_exists:
                    print(f"Error: Product name '{product_name}' already exists. Please enter a different product name.")
                else:
                    break 
            stock.add_product(
                product_id,
                product_name,
                int(input("Enter total price: ")),
                int(input("Enter quantity: "))
            )
            break  # Exit the loop after successful addition

