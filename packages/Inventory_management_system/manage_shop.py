
# This file not will run from this location this file allow run all module file. this file inside package and it will run from main.py outside this folder


import os, time

import adding_product_in_stock
import check_stock_report
import update_prduct_in_stock
import all_stocks_in_inventory



def my_stock(user_name, user_id):
    user_file = f"{user_name}'s_stock_{user_id}.json"
    JSON_data = r"data_base/inventory_data/" + user_file
    
    if os.name == 'nt':  # For Windows
        os.system('cls')

    while True:
        input("\nPress Enter to Dashboard: ")
        for i in range(3):
            time.sleep(.1)
            print(".",end ="")
        print( "\n\n******************************************************************" )
        print(f".............Welcome back, {user_name}!.............")
        print( "**********************************************************************" )

        print("1. Add new product in stock")
        print("2. Update Inventory")
        print("3. Check stock Report")
        print("4. My_inventory")
        print("0. Log out")   


        try:
            choice = int(input("Enter your choice: "))        

            if choice==1:
                adding_product_in_stock.add_product_in_stock(JSON_data, exiting_program)
            elif choice==2:
                update_prduct_in_stock.update_product(JSON_data, exiting_program)
            elif choice==3:
                check_stock_report.all_product_information(JSON_data, exiting_program)
            elif choice==4:
                all_stocks_in_inventory.my_inventory(JSON_data, exiting_program)
            
            
            elif choice==0:
                print("\nLoging out",end="")
                for i in range(8):
                    time.sleep(0.3)
                    print(".",end="")

                if os.name == 'nt':  # For Windows
                    os.system('cls')

                break
                
            else:
                print("Please enter valid choise no...")
                exiting_program()

        except ValueError:
            print("Oh! Please enter an integer value.")
            exiting_program()
            
def exiting_program():
    print("Exiting to dashboard",end="")
    for i in range(10):
        time.sleep(0.1)
        print(".",end="")
    print("\n")

