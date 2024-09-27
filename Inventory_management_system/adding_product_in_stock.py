import json, os

# Path to the JSON file
JSON_data = r"S:\python_project(inventory_management_system)\Indixpert-FSD-April-Python-Pr04\stock.json"

def add_product_in_stock():
    class Inventory:

        def add_product(self, id, name, price, quantity):
            dict_format_item = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            new_product = {id: dict_format_item}

            if os.path.exists(JSON_data):
                with open(JSON_data, "r") as file:
                    try:
                        list_data = json.load(file)
                    except json.JSONDecodeError:
                        list_data = []
            else:
                list_data = []

            list_data.append(new_product)

            with open(JSON_data, "w") as file:
                file.write(json.dumps(list_data, indent=2) )
                # json.dump(list_data, file)

            print("Product added successfully in your stock.")

    stock = Inventory()

    stock.add_product(
        int(input("Product ID: ")), 
        input("Enter product name: "), 
        int(input("Enter total price: ")), 
        int(input("Enter quantity no: "))
    )
