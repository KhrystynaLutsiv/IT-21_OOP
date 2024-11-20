class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.name} - Price: {self.price} USD, Quantity: {self.quantity} units"


class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Customer: {self.name}, Contact: {self.contact}"


class Supplier:
    def __init__(self, name, contact, terms):
        self.name = name
        self.contact = contact
        self.terms = terms

    def __str__(self):
        return f"Supplier: {self.name}, Contact: {self.contact}, Terms: {self.terms}"


class Sale:
    def __init__(self, product, quantity, customer):
        self.product = product
        self.quantity = quantity
        self.customer = customer
        self.total_price = product.price * quantity

    def process_sale(self):
        if self.product.quantity >= self.quantity:
            self.product.update_quantity(-self.quantity)
            print(f"Sale processed for {self.customer.name}. Total price: {self.total_price} USD")
        else:
            print(f"Not enough {self.product.name} in stock for the sale.")

    def __str__(self):
        return f"Sale: {self.quantity} units of {self.product.name} to {self.customer.name}."


# Створення баз даних для товарів, клієнтів, постачальників та продажів
products = []
customers = []
suppliers = []
sales = []

# Функції для роботи з даними
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    product = Product(name, price, quantity)
    products.append(product)
    print(f"Product {name} added successfully.\n")


def add_customer():
    name = input("Enter customer name: ")
    contact = input("Enter customer contact: ")
    customer = Customer(name, contact)
    customers.append(customer)
    print(f"Customer {name} added successfully.\n")


def add_supplier():
    name = input("Enter supplier name: ")
    contact = input("Enter supplier contact: ")
    terms = input("Enter supplier terms: ")
    supplier = Supplier(name, contact, terms)
    suppliers.append(supplier)
    print(f"Supplier {name} added successfully.\n")


def process_sale():
    if len(products) == 0:
        print("No products available for sale.\n")
        return

    if len(customers) == 0:
        print("No customers found.\n")
        return

    print("Available products:")
    for idx, product in enumerate(products):
        print(f"{idx + 1}. {product}")

    product_index = int(input("Select product (by number): ")) - 1
    product = products[product_index]

    print("Available customers:")
    for idx, customer in enumerate(customers):
        print(f"{idx + 1}. {customer}")

    customer_index = int(input("Select customer (by number): ")) - 1
    customer = customers[customer_index]

    quantity = int(input("Enter quantity to sell: "))

    sale = Sale(product, quantity, customer)
    sale.process_sale()
    sales.append(sale)


def display_inventory():
    print("\nCurrent Inventory:")
    for product in products:
        print(product)
    print()


def display_customers():
    print("\nList of Customers:")
    for customer in customers:
        print(customer)
    print()


def display_sales():
    print("\nSales History:")
    for sale in sales:
        print(sale)
    print()

# Головне меню програми
def main():
    while True:
        print("\n=== Mineral Fertilizer Trading System ===")
        print("1. Add Product")
        print("2. Add Customer")
        print("3. Add Supplier")
        print("4. Process Sale")
        print("5. Display Inventory")
        print("6. Display Customers")
        print("7. Display Sales")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            add_customer()
        elif choice == '3':
            add_supplier()
        elif choice == '4':
            process_sale()
        elif choice == '5':
            display_inventory()
        elif choice == '6':
            display_customers()
        elif choice == '7':
            display_sales()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Запуск програми
if __name__ == "__main__":
    main()

##Рефакторинг##
class InventoryManager:
    def __init__(self):
        self.products = []
        self.customers = []
        self.suppliers = []
        self.sales = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"Product {name} added successfully.\n")

    def add_customer(self, name, contact):
        customer = Customer(name, contact)
        self.customers.append(customer)
        print(f"Customer {name} added successfully.\n")

    def add_supplier(self, name, contact, terms):
        supplier = Supplier(name, contact, terms)
        self.suppliers.append(supplier)
        print(f"Supplier {name} added successfully.\n")

    def process_sale(self, product, quantity, customer):
        sale = Sale(product, quantity, customer)
        sale.process_sale()
        self.sales.append(sale)

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for product in self.products:
            print(product)
        print()

    def display_customers(self):
        print("\nList of Customers:")
        for customer in self.customers:
            print(customer)
        print()

    def display_sales(self):
        print("\nSales History:")
        for sale in self.sales:
            print(sale)
        print()

    def select_product(self):
        print("Available products:")
        for idx, product in enumerate(self.products):
            print(f"{idx + 1}. {product}")
        product_index = int(input("Select product (by number): ")) - 1
        return self.products[product_index]

    def select_customer(self):
        print("Available customers:")
        for idx, customer in enumerate(self.customers):
            print(f"{idx + 1}. {customer}")
        customer_index = int(input("Select customer (by number): ")) - 1
        return self.customers[customer_index]


class UIManager:
    def __init__(self, inventory_manager):
        self.inventory_manager = inventory_manager

    def main_menu(self):
        while True:
            print("\n=== Mineral Fertilizer Trading System ===")
            print("1. Add Product")
            print("2. Add Customer")
            print("3. Add Supplier")
            print("4. Process Sale")
            print("5. Display Inventory")
            print("6. Display Customers")
            print("7. Display Sales")
            print("8. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                self.inventory_manager.add_product(name, price, quantity)
            elif choice == '2':
                name = input("Enter customer name: ")
                contact = input("Enter customer contact: ")
                self.inventory_manager.add_customer(name, contact)
            elif choice == '3':
                name = input("Enter supplier name: ")
                contact = input("Enter supplier contact: ")
                terms = input("Enter supplier terms: ")
                self.inventory_manager.add_supplier(name, contact, terms)
            elif choice == '4':
                product = self.inventory_manager.select_product()
                customer = self.inventory_manager.select_customer()
                quantity = int(input("Enter quantity to sell: "))
                self.inventory_manager.process_sale(product, quantity, customer)
            elif choice == '5':
                self.inventory_manager.display_inventory()
            elif choice == '6':
                self.inventory_manager.display_customers()
            elif choice == '7':
                self.inventory_manager.display_sales()
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.\n")


# Запуск програми
if __name__ == "__main__":
    inventory_manager = InventoryManager()
    ui_manager = UIManager(inventory_manager)
    ui_manager.main_menu()

