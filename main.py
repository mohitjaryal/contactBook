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
    if not contacts:
        print('No contact found')
        return
    print('\n All contacts')
    print("-" * 30)
    for name,info in contacts.items():
        print("Name : '{name}'")
        print("Phone : '{info['phone]}'")
        print("Email : '{info['email]}'")
        print("-" * 30)

# Search contact
def search_contacts(contacts):
    search_name = input('Enter contact name to search :').title()
    if search_name in contacts:
        info = contacts[search_name]
        print(f"\n🔍 Found Contact:")
        print(f"Name: {search_name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")


# Delete contact
def delete_contact(contacts):
    del_name = input('Enter contact name to delete :')
    if del_name in contacts:
        del contacts[del_name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{del_name}' deleted successfully!")
    else:
        print("Contact not found !")