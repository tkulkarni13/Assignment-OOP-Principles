# Task 1: Create Base Product Class

# Base product class with has a product id, name, and price
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    # Function to display product info
    def display_product_info(self):
        print(f"{self.product_id}: {self.name} ${self.price}")

# Task 2: Implement Subclasses for Specific Products

# Book class is similar to product, but there is also an author
class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    # Task 3: Override Display Method in Subclasses

    def display_product_info(self):
        print(f"{self.product_id}: {self.name} by {self.author} ${self.price}")

# Electronic class is similar to product, but there is also info about specs
class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs
    
    def display_product_info(self):
        print(f"{self.product_id}: {self.name} with {self.specs} ${self.price}")

# Clothing class is similar to product, but there is also size
class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_product_info(self):
        print(f"{self.product_id}: {self.name}, Size: {self.size} ${self.price}")

# Task 4: Test Product Catalog Functionality

my_product = Product("101", "Bicycle", 400)
my_product.display_product_info()

my_book = Book("102", "Python Fundamentals", 29.99, "J. Doe")
my_book.display_product_info()

my_electronic = Electronic("103", "Laptop", 700, "256 GB storage")
my_electronic.display_product_info()

my_clothing = Clothing("104", "T-Shirt", 5.99, "XL")
my_clothing.display_product_info()