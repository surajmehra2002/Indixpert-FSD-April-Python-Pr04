import sys
sys.path.append(r"S:\indixpert_coaching\python_project\Indixpert-FSD-April-Python-Pr04\Inventory_management_system")  #because line no 4 to 8 module importing

import adding_product_in_stock


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
                adding_product_in_stock.add_product_in_stock()
            elif choice==2:
                pass
            elif choice==3:
                pass
            elif choice==4:
                pass
            elif choice==0:
                break
            else:
                print("Please enter valid choise no...")

        except ValueError:
            print("Oh! Please enter an integer value.")
            
        