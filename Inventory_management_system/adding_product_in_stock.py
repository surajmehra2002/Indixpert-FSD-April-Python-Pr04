def add_product_in_stock():
    class Inventory:
        def __init__(self):
            # Initialize an empty dictionary to store products
            self.stock = {}

        def add_product(self, name, price, quantity):
            # Add the product to the inventory
            if name in self.stock:
                # If the product already exists, update the quantity
                self.stock[name]['quantity'] += quantity
            else:
                # Add new product to the stock
                self.stock[name] = {'price': price, 'quantity': quantity}

        def show_inventory(self):
            # Display the inventory
            if not self.stock:
                print("Inventory is empty.")
            else:
                for product, details in self.stock.items():
                    print(f"Product: {product}, Price: {details['price']}, Quantity: {details['quantity']}")

    # Create an instance of Inventory
    stock = Inventory()

    # Add some products
    # stock.add_product("milk", 1000, 50)
    # stock.add_product("bread", 50, 30)
    stock.add_product(input("Enter product name: "), int(input("Enter totle price: ")), int(input("Enter quantity no: ")))

    # Display the inventory
    stock.show_inventory()

       
    print("Product added successfully in your stock")