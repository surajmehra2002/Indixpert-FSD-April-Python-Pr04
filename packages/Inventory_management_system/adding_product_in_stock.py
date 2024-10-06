import json
import os
import time
from datetime import datetime


def add_product_in_stock(JSON_data, exiting_program):

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

            with open(JSON_data, "w") as file:
                json_data = json.dumps(list_data, indent=None, separators=(",", ":"))
                compact_json_data = json_data.replace("},", "}, \n")
                compact_json_data1 = compact_json_data.replace('[', '[ \n')
                compact_json_data2 = compact_json_data1.replace(']', '\n ]')
                compact_json_data3 = compact_json_data2.replace(',"product":', ',\n "product":')
                compact_json_data4 = compact_json_data3.replace('}}, ', '}}, \n')
                file.write(compact_json_data4)
            print("\nAdding", end="")
            for i in range(5):
                time.sleep(.2)
                print(".", end="")
            print("\nProduct added successfully to your stock.")

    stock = Inventory()

    def count_user():
        count_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data_base', 'count_user.json'))
        if os.path.exists(count_file):
            with open(count_file, "r") as file:
                try:
                    data = json.load(file)
                    count = data["total_user"]
                except json.JSONDecodeError:
                    count = 0
        else:
            count = 0
            data = {"total_user": count + 1}
            os.makedirs(os.path.dirname(count_file), exist_ok=True)
            with open(count_file, "w") as file:
                json.dump(data, file, indent=4)

        return count

    def update_count_file(count):
        count_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data_base', 'count_user.json'))
        with open(count_file, "w") as file:
            json.dump({"total_user": count}, file, indent=4)

    if os.path.exists(JSON_data):
        with open(JSON_data, "r") as file:
            try:
                list_data = json.loads(file.read())
            except json.JSONDecodeError:
                list_data = []
    else:
        print("Oh! You are a new user")
        print("Creating database file", end="")
        for i in range(5):
            time.sleep(.1)
            print(".", end="")
        print("\n")
        list_data = []

    system_generate_id = count_user() + 1
    product_id = "PD0" + str(system_generate_id)

    update_count_file(system_generate_id)

    while True:
        product_name = input("Enter Product Name: ").strip()
        product_name_exists = any(product["product"]["name"].lower() == product_name.lower() for product in list_data)

        if product_name_exists:
            print(f"Error: Product name '{product_name}' already exists. Please enter a different product name.")
        else:
            break

    stock.add_product(
        product_id,
        product_name,
        int(input("Enter per item price: ")),
        int(input("Enter quantity: "))
    )
