import json,sys, time
sys.path.append(r"S:\python_project(inventory_management_system)\Indixpert-FSD-April-Python-Pr04\Inventory_management_system")  #because line no 4 to 8 module importing
import uuid
import re  # Import the re module for regular expressions
import manage_shop



User_login_data = r"user_data.json"

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
    return "INVEN" + str(uuid.uuid4())[:5]  

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_email_resistered(user_email):
    users = load_user_data()
    for user in users:
        if user["email"]==user_email:
            return True
        else:
            return False  


def valid_password(new_password):
    if len(new_password)>=8:
        return True
    
def user_authenticated(user_name, user_id):
    manage_shop.my_stock(user_name, user_id)

def opening_dashboard():
    print("\n\nLoading your Dashboard", end="")
    for i in range (10):
        time.sleep(.3)
        print(".", end="")


def user_sign_up_data():
    users = load_user_data()

    if len(users) >= 3:
        print("Registration limit reached. Only 3 users can sign up.")
        return

    user_id = generate_user_id() 
    first_name = input("Your first name: ").strip()
    last_name = input("Last name: ").strip()
    user_email = input("Email ID: ").strip()

    if not validate_email(user_email):
        print("Error: Invalid email format. Please enter a valid email address.")
        return

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
        print("User registered successfully!")
    else:
        print("Passwords do not match. Try again.")

def user_login_data():
    user_email = input("Email ID: ").strip()

    if not validate_email(user_email):
        print("Invalid email format. Please enter a valid email address.")
        return False

    password = input("User password: ").strip()

    users = load_user_data()

    for user in users:
        if user["email"] == user_email and user["password"] == password:
            print(f"Welcome back, {user['first_name']}!")
            opening_dashboard()
            user_authenticated(user["first_name"], user["user_id"])
            return True
    print("Invalid email or password. Please try again.")
    return False


def dashboard():
    print("\n*************** Welcome to Inventory Management System **************\n\n")
    while True:
        print("1: Log in")
        print("2: Sign Up")
        print("0: Exit")

        try:
            choice = int(input("Enter 1 for login, for new user Enter 2 for sign up: ").strip())

            if choice == 1:
                if user_login_data():
                    break

            elif choice == 2:
                user_sign_up_data()

            elif choice == 0:
                break

            else:
                print("Error: Please enter a valid choice.")

        except ValueError:
            print("Only integer values are allowed.")
