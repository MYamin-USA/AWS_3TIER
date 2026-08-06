import csv
import os

class Product:
    def __init__(self, sku, name, price, category):
        self.sku = sku
        self.name = name
        self.price = float(price)
        self.category = category

class InventoryManager:
    def __init__(self, filename='inventory_data.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['SKU', 'Name', 'Price', 'Category'])

    def add_product(self, product):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([product.sku, product.name, product.price, product.category])

    def get_all_products(self):
        if not os.path.exists(self.filename): return []
        with open(self.filename, 'r') as f:
            return list(csv.DictReader(f))