
import json
JSON_data = r"S:\python_project(inventory_management_system)\Indixpert-FSD-April-Python-Pr04\stock.json"



def update_product():
    product_id = int(input("Enter product id which you want update: "))

    with open(JSON_data , "r") as file:
        data = json.loads(file.read())
        for product in data:
            if product_id in product:
                print(f"Current data for product {product_id}: {product[product_id]}")
                
                # Take new values for the product attributes
                new_name = input("Enter new product name: ")
                new_price = int(input("Enter new product price: "))
                new_quantity = int(input("Enter new product quantity: "))
                
                # Update the product's attributes
                product[product_id]['name'] = new_name
                product[product_id]['price'] = new_price
                product[product_id]['quantity'] = new_quantity
                
                print(f"Updated data for product {product_id}: {product[product_id]}")
                break
        else:
            print("Product not found.")



