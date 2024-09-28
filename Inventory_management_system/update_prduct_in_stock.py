
# This file not will run from this location because it is module and all files manage from manage_shop.py


import json
import os
from datetime import datetime


def update_product(JSON_data):
    print("To exit, enter '0' as the product ID.")
    product_id_input = input("Enter product id which you want to update: ")

    if product_id_input == '0':
        print("Exiting to dashboard.")
        return  

    try:
        product_id = int(product_id_input)
    except ValueError:
        print("Invalid input. Please enter a valid product ID.")
        return  

    if not os.path.exists(JSON_data):
        print("The stock file does not exist.")
        return

    with open(JSON_data, "r") as file:
        data = json.loads(file.read())
        product_found = False 
        for product in data:
            if product["product_id"] == product_id: 
                product_found = True
                print(f"Current data for product {product_id}: {product['product']}")
                
                current_name = product["product"]["name"]

                new_name = input("Enter new product name (or press enter to keep current): ")

                if new_name and new_name.lower() != current_name.lower():
                    existing_product = next((p for p in data if p["product"]["name"].lower() == new_name.lower() and p["product_id"] != product_id), None)
                    if existing_product:
                        print(f"Error: Product name '{new_name}' already exists for product ID {existing_product['product_id']}.")
                        return 
                if new_name:
                    product["product"]["name"] = new_name
                
                new_price = input("Enter new product price: ")
                if new_price:
                    product["product"]["price"] = int(new_price)
                
                new_quantity = int(input("Enter additional quantity to add: "))
                
                if new_name == current_name or not new_name:
                    product["product"]["quantity"] += new_quantity  
                else:
                    product["product"]["quantity"] = new_quantity

                product["product"]["added_on"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print(f"Updated data for product {product_id}: {product['product']}")
                break

        if not product_found:
            print("Product not found.")

    with open(JSON_data, "w") as file:
        json.dump(data, file, indent=2)

