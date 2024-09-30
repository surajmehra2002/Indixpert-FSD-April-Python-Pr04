# This file will not run from this location because it is a module, and all files are managed from manage_shop.py

import json
import os
from datetime import datetime

def update_product(JSON_data, exiting_program):
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
    
            print("To exit, enter '0' as the product ID.")
            product_id_input = input("Enter product id which you want to update: ").strip()

            if product_id_input == '0':
                exiting_program()
                return  
            
            product_id = product_id_input.upper()

            with open(JSON_data, "r") as file:
                data = json.loads(file.read())
                product_found = False 
                for product in data:
                    if product["product_id"] == product_id: 
                        product_found = True
                        print(f"Current data for product {product_id}: {product['product']} \n")
                        print("What would you like to do with this product?")
                        print("1. Restore ")
                        print("2. Sell ")
                        choice = input("Enter your choice (1 for restore, 2 for sell): ")

                        if choice == '1':
                            try:
                                qty_to_add = int(input("Enter the quantity to restore: "))
                                product["product"]["quantity"] += qty_to_add
                                product["product"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                print(f"{qty_to_add} units added to product ID {product_id}. New quantity: {product['product']['quantity']}")
                            except ValueError:
                                print("Invalid input. Quantity should be numbers.")
                            
                        elif choice == '2':
                            try:
                                qty_to_sell = int(input("Enter the quantity to sell: "))
                                if qty_to_sell > product["product"]["quantity"]:
                                    print("Error: Selling quantity exceeds available stock.")
                            
                                    
                                else:
                                
                                    remaining_qty = product["product"]["quantity"] - qty_to_sell
                                    product["product"]["quantity"] = remaining_qty
                                    product["product"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        
                                    print(f"{qty_to_sell} units sold from product ID {product_id}. New quantity: {product['product']['quantity']}")
                                    
                                    # Check if all products are sold
                                    if remaining_qty == 0:
                                        print("Your products are out of stock, please restore as fast as possible.")
                                        restore_choice = input("Will you restore? (yes/no): ").lower()
                                        if restore_choice == 'yes':
                                            print("Your product will be kept.")
                                            exiting_program()
                                        else:
                                            data.remove(product) 
                                            print(f"Product ID {product_id} has been removed from the inventory.")
                                            exiting_program()
                            except ValueError:
                                print("Invalid input. Quantity and price should be numbers.")
                        else:
                            print("Invalid choice. Please enter 1 or 2.")
                        break

                if not product_found:
                    print("Product not found.")

            with open(JSON_data, "w") as file:
                json.dump(data, file, indent=2)

