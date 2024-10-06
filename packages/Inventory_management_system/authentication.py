import json,sys,os, time
import uuid
from admin.admin_dashboard import admin_login

import re 
# sys.path.append(r"S:\python_project(inventory_management_system)\Indixpert-FSD-April-Python-Pr04\Inventory_management_system")  #because line no 4 to 8 module importing
sys.path.append(os.path.dirname(__file__))




User_login_data = r"data_base/users/user_list.json"

def save_user_data(data):
    try:
        with open(User_login_data, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    users.append(data)

    with open(User_login_data, 'w') as file:
        json.dump(users, file, indent=4)

def load_user_data():
    try:
        with open(User_login_data, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def generate_user_id():
    return "SN" + str(uuid.uuid4())[:5]  

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_email_resistered(user_email):
    users = load_user_data()
    for user in users:
        if user["email"]==user_email:
            return True
            
         


def valid_password(new_password):
    if len(new_password)>=8:
        return True
    
def user_authenticated(user_name, user_id):
    import manage_shop
    manage_shop.my_stock(user_name, user_id)
    

def opening_dashboard():
    print("\n\nLoading your Dashboard", end="")
    for i in range (10):
        time.sleep(.3)
        print(".", end="")

def user_sign_up_data():
    users = load_user_data()

    if len(users) >= 10:
        print("Registration limit reached. Only 3 users can sign up.")
        return

    user_id = generate_user_id() 
    first_name = input("Your first name: ").strip()
    last_name = input("Last name: ").strip()

    while True:
        user_email = input("Email ID: ").strip()
        if not validate_email(user_email):
            print("Error: Invalid email format. Please enter a valid email address.")
            
        else:
            break

    if is_email_resistered(user_email):
        print(f"User already registered with this email: {user_email}")
        return
    
    while True:
        new_password = input("Create Password: ").strip()
        
        if valid_password(new_password):
            break
        else:
            print("Password must be at least 8 characters long. Please try again.")

    confirm_password = input("Confirm Password: ").strip()

    if new_password == confirm_password:
        new_user = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": user_email,
            "password": new_password
        }
        save_user_data(new_user)
        print("User registered successfully!\n")
    else:
        print("Passwords do not match. Try again.\n")

def user_login_data():
    while True:
        user_email = input("Email ID: ").strip()
        if not validate_email(user_email):
            print("Invalid email format. Please enter a valid email address.")
        else:
            break
        

    password = input("User password: ").strip()

    users = load_user_data()

    flag = False
    for user in users:
        if user["email"] == user_email:
            if user["password"] == password:
                
                opening_dashboard()
                user_authenticated(user["first_name"], user["user_id"])
                return 
            else:
                print("Invalid password. Please try again.")
                return
        else:
            flag = True
    if flag:
        print("Sorry! You are new user, Please Sign Up first")
    return False


# main functions from here:
def normal_user():
    while True:
        print("\n1: Log In")
        print("2: Sign up")
        print("3: Main menu")
        try:
            choice = int(input("Enter choice: ").strip())
            if choice == 1:
                user_login_data()
                
                    
            elif choice == 2:
                user_sign_up_data()
                

            elif choice == 3:
                break

            else:
                print("Not valid input\n")
        except ValueError:
            print("Enter integer value")

     
def dashboard():
    print("\n*************** Welcome to Inventory Management System **************\n")
    while True:
        print("\n1: Normal User")
        print("2: Admin")
        print("0: Exit")

        try:
            choice = int(input("Enter choice: ").strip())

            if choice == 1:
                normal_user()     
                                                       

            elif choice == 2:
                admin_login()

            elif choice == 0:
                break

            else:
                print("Error: Please enter a valid choice.")

        except ValueError:
            print("Only integer values are allowed.")
# dashboard()
