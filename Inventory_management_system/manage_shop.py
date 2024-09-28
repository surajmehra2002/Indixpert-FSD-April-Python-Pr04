
# This file not will run from this location this file allow run all module file. this file inside package and it will run from main.py outside this folder


import sys
sys.path.append(r"S:\indixpert_coaching\python_project\Indixpert-FSD-April-Python-Pr04\Inventory_management_system")  #because line no 4 to 8 module importing
JSON_data = r"S:\indixpert_coaching\python_project\Indixpert-FSD-April-Python-Pr04\stock.json"

import adding_product_in_stock
import check_stock_report
import update_prduct_in_stock


def my_stock():

    while True:
        print( "\n\n****************************************************" )
        print(".............Inventory Management System.............")
        print( "****************************************************" )

        print("1. Add new product in stock")
        print("2. Update Inventory")
        print("3. Check stock Report")
        print("4. Search product in stock ")
        print("0. Exit")   


        try:
            choice = int(input("Enter your choice: "))        

            if choice==1:
                adding_product_in_stock.add_product_in_stock(JSON_data)
            elif choice==2:
                update_prduct_in_stock.update_product(JSON_data)
            elif choice==3:
                check_stock_report.all_product_information(JSON_data)
                pass
            elif choice==4:
                pass
            elif choice==0:
                break
            else:
                print("Please enter valid choise no...")

        except ValueError:
            print("Oh! Please enter an integer value.")
            
        