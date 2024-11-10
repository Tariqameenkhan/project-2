# inventory_management_system
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
# p1= products(1,"chair",any,100,20)
# print(p1.category,p1.name,p1.price,p1.product_id,p1.stock)
class ims:
    LOW_STOCK = 4  
    def __init__(self):
        self.products = {}  
        self.users = {
            "admin": {"password": "admin123", "role": "Admin"},
            "user": {"password": "user123", "role": "User"}
        }
        self.current_user = None  
# i=ims()
# print(i.users["user"])
# print(i.users["admin"])

    def login(self, username, password):
        try:
            if username in self.users and self.users[username]["password"] == password:
                self.current_user = self.users[username]
                print(f"Login successful! Logged in as {self.current_user['role']}.")
            else:
                raise ValueError("Invalid username or password.")
        except ValueError as e:
            print(e)
# i=ims()
# print(i.users["us"])
# print(i.users["admin"])
    def check_admin(self):
        if not self.current_user or self.current_user["role"] != "Admin":
            raise PermissionError("Access denied. Only Admins can perform this action.")

    def add_product(self, product_id, name, category, price, stock_quantity):
        try:
            self.check_admin()
            if product_id in self.products:
                raise KeyError("Product ID already exists.")
            product = Product(product_id, name, category, price, stock_quantity)
            self.products[product_id] = product
            print(f"Product '{name}' added successfully.")
        except (PermissionError, KeyError) as e:
            print(e)

    def delete_product(self, product_id):
        try:
            self.check_admin()
            if product_id not in self.products:
                raise KeyError("Product ID not found.")
            deleted_product = self.products.pop(product_id)
            print(f"Product '{deleted_product.name}' deleted successfully.")
        except (PermissionError, KeyError) as e:
            print(e)

    def edit_product(self, product_id, **kwargs):
        try:
            self.check_admin()
            if product_id not in self.products:
                raise KeyError("Product ID not found.")
            product = self.products[product_id]
            for key, value in kwargs.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            print(f"Product '{product.name}' updated successfully.")
        except (PermissionError, KeyError) as e:
            print(e)

    def view_inventory(self):
        if self.products:
            print("Inventory:")
            for product in self.products.values():
                self.display_product(product)
                if product.stock_quantity < self.LOW_STOCK:
                    print(f"Warning: Product '{product.name}' is low on stock. Please restock.")
        else:
            print("Inventory is empty.")

    def search_product(self, name=None, category=None):
        found = False
        for product in self.products.values():
            if (name and product.name.lower() == name.lower()) or \
               (category and product.category.lower() == category.lower()):
                self.display_product(product)
                found = True
        if not found:
            print("No products found ! .")

    def filter_by_stock_level(self, low_stock=False):
        print("Low Stock Products:" if low_stock else "In Stock Products:")
        for product in self.products.values():
            if (low_stock and product.stock_quantity < self.LOW_STOCK) or \
               (not low_stock and product.stock_quantity >= self.LOW_STOCK):
                self.display_product(product)

    def adjust_stock(self, product_id, quantity):
        try:
            self.check_admin()
            if product_id not in self.products:
                raise KeyError("Product ID not found.")
            product = self.products[product_id]
            new_stock = product.stock_quantity + quantity
            if new_stock < 0:
                raise ValueError("Insufficient stock. Cannot reduce below zero.")
            product.stock_quantity = new_stock
            action = "restocked" if quantity > 0 else "reduced"
            print(f"Product '{product.name}' stock {action} by {abs(quantity)} units. New stock: {product.stock_quantity}.")
        except (PermissionError, KeyError, ValueError) as e:
            print(e)

    def display_product(self, product):
        print(f"ID: {product.product_id}, Name: {product.name}, "
              f"Category: {product.category}, Price: ${product.price}, "
              f"Stock: {product.stock_quantity}")

im=ims()
im.login("admin", "admin123")  

im.add_product(1, "Laptop", "Electronics", 999.99, 10)
im.add_product(2, "Chair", "Table", 49.99, 3)

im.view_inventory()

im.search_product(name="Chair")
im.search_product(name="Laptop")

im.filter_by_stock_level(low_stock=True)

im.adjust_stock(2, 5)   
im.adjust_stock(2, -20) 

im.login("user", "user123")
im.add_product(3, "Desk", "Table", 150.00, 5) 
im.delete_product(1) 
im.login("us", "us123")