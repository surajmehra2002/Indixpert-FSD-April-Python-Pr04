import json
JSON_data = r"S:\python_project(inventory_management_system)\Indixpert-FSD-April-Python-Pr04\stock.json"

def all_product_information():
    with open (JSON_data, "r") as file:
        
        data = json.load(file)
        print(f"Totle {len(data)} products are available")
        for student in data:
            print(student)
