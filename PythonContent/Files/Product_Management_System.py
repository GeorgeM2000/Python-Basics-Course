import json
import os

# Where json function
def where_json(file_name):
    return os.path.exists(file_name)

# Promt user function
def promt_user():
    print("To call set() enter    1.\nTo call list() enter   2.\nTo call import() enter 3.\nTo call export() enter 4.\nTo exit enter          5.")
    return int(input())

# List function
def list(file, id):
    with open(file, "r") as json_file:
        id_found = False
        products = json.load(json_file)
        for key in products.keys():
            if key == id:
                id_found = True
                print(products[key])
                break
        
    if not id_found:
        print("Not found.")
            
# Set function
def set(id, quantity):
    json_file = open("Products_Stock.json", "r+")
    products = json.load(json_file)

    id_found = False
    for key in products.keys():
        if key == id:
            id_found = True
            products[id] = quantity
            break
        
    if not id_found:
        products[id] = quantity

    json_file.close()

    json_file = open("Products_Stock.json", "w")
    json.dump(products, json_file)
    json_file.close()

# Import function
def importFile(file):
    json_file = open(file, "r")
    products = json.load(json_file)
    for key, value in products.items():
        print(f'ID : {key}      Quantity : {value}')

    json_file.close()

# Export function
def export(src_file, dest_file):
    source_file = open(src_file, "r")
    destination_file = open(dest_file, "w")

    products = json.load(source_file)
    json.dump(destination_file, products)

    source_file.close()
    destination_file.close()

if __name__ == "__main__":

    # If 'Products_Stock.json' file doesn't exist
    if not where_json('Products_Stock.json'):
        products_file = open("Products_Stock.json", "w")
        products_file.close()

    # If 'Products_Stock.json' file exists
    if where_json('Products_Stock.json'):
 
        user_input = promt_user()
        while(user_input != 5):

            # Set
            if user_input == 1:
                id = int(input("Enter the product id : "))
                quantity = int(input("Enter the product quantity : "))
                file_path = input("Enter the file path (C:\\path\\to\\file) : ")

                set(file_path, id, quantity)
            # List
            elif user_input == 2:
                id = int(input("Enter the product id : "))
                file_path = input("Enter the file path (C:\\path\\to\\file) : ")

                list(file_path, id)
            # Import
            elif user_input == 3:
                importFile(input("Enter the file path (C:\\path\\to\\file) : "))
            # Export
            elif user_input == 4:
                source_file = input("Enter the source file path (C:\\path\\to\\file) : ")
                destination_file = input("Enter the destination file path (C:\\path\\to\\file) : ")

                export(source_file, destination_file)

            user_input = function()


