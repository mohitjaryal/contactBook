# Contact Book made with python

import os

CONTACTS_FILE = 'contact.txt'

# Load contacts from file
def load_contacts():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone, email = line.strip().split("|")
                contacts[name] = {"phone": phone, "email": email}
    return contacts

# Save contacts 
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name}|{info['phone']}|{info['email']}\n")


# Add new contact
def add_contact(contacts):
    name = input("Enter name :").title()
    phone = input('Enter phone number :')
    email = input('Enter email address :')
    contacts[name] = {'phone':phone,'email':email}
    save_contacts()
    print(f"Contact '{name}'added sucessfully")

    
# View all contacts
def view_contacts(contacts):
    