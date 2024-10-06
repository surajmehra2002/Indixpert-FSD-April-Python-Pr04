import os
import json

User_login_data = r"data_base/users/user_list.json"

def admin_login():
    admin_email = "suraj@gmail.com"
    admin_password = "suraj123"
    
    print("\nAdmin Login")
    while True:
        user_email = input("Enter Admin Email: ").strip()
        user_password = input("Enter Admin Password: ").strip()

        if user_email == admin_email and user_password == admin_password:
            print("Login successful! Opening Admin Dashboard...")
            admin_dashboard()  
            break
        else:
            print("Invalid email or password. Please try again.\n")

def admin_dashboard():
    while True:
        print("\n*************** Admin Dashboard ***************")
        print("1: Check Product")
        print("2: Remove User")
        print("3: Exit")
        
        try:
            choice = int(input("Enter choice: ").strip())
            
            if choice == 1:
                check_product() 
            elif choice == 2:
                remove_user() 
            elif choice == 3:
                print("Exiting Admin Dashboard...")
                break
            else:
                print("Error: Please enter a valid choice.")
        except ValueError:
            print("Only integer values are allowed.")

def check_product():
    all_products = []
    inventory_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data_base', 'inventory_data')
    
    for file_name in os.listdir(inventory_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(inventory_path, file_name)
            with open(file_path, 'r') as file:
                try:
                    products = json.load(file)
                except json.JSONDecodeError:
                    continue
                
                all_products.extend(products)

    print("\nTotal Products:")
    for product in all_products:
        print(f"Product ID: {product['product_id']}")
    
    print(f"Total number of products: {len(all_products)}\n")

    product_id_to_check = input("Enter the Product ID you want to check: ").strip().upper()

    product_found = False

    for product in all_products:
        if product["product_id"] == product_id_to_check:
            print(f"\nProducts for User: {file_name.split('.')[0]}")
            print(f"Product ID: {product['product_id']}")
            print(f"Name: {product['product']['name']}")
            print(f"Price: {product['product']['price']}")
            print(f"Quantity: {product['product']['quantity']}")
            print(f"Added on: {product['product']['added_on']}")
            print("------------------------------")
            product_found = True

    if not product_found:
        print("Product not found. Please enter a valid Product ID.")

    input("Press Enter to return to the Admin Dashboard...")

def remove_user():
    users = load_user_data()

    if not users:
        print("No users found.")
        input("Press Enter to return to the Admin Dashboard...")
        return

    print("\nCurrent Users:")
    for user in users:
        print(f"User Email: {user['email']}")

    user_email_to_remove = input("\nEnter the email of the user you want to remove: ").strip()

    user_found = False
    for user in users:
        if user["email"] == user_email_to_remove:
            users.remove(user)
            user_found = True
            break

    if user_found:
        with open(User_login_data, 'w') as file:
            json.dump(users, file, indent=4)
        print(f"User with email '{user_email_to_remove}' has been removed successfully.")
        
        if not users:
            print("All users have been removed.")
    else:
        print(f"No user found with email '{user_email_to_remove}'.")

    input("Press Enter to return to the Admin Dashboard...")

def load_user_data():
    try:
        with open(User_login_data, 'r') as file:
            return json.load(file)  
    except FileNotFoundError:
        return []
