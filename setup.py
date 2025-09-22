import json
import os

# TODO: May need to make a user via the CLI

# This is for setting up the json file.
DATA_FILE = 'static/json/setup.json'

def save_json(data):
    with open(DATA_FILE,'w') as f:
        json.dump(data,f,indent=4)
        print(" Data added to ",DATA_FILE)

def load_json():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def create_documentation_for_business():
    brand = input("Name of Company:")
    about = input("About the Company:")

    data = {
        "Brand": brand,
        "About": about
            }
    
    save_json(data)

def menu():
    while True:
        print("\n======== CREATE DOCUMENTAION ========")
        print("1.Add Documentation")
        print("2.Exit")

        choice = input("Choose an Option:").strip()

        if choice == '1':
            create_documentation_for_business()
        elif choice == '2':
            print("Exiting")
            break
        else:
            print("Incorrect Input")

if __name__ == '__main__':
    menu()
