import pickle

# Define the file where contacts will be stored
CONTACTS_FILE = 'contacts.pkl'

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'wb') as file:
        pickle.dump(contacts, file)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print("Contact added successfully.")

# View the contact list
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

# Search for a contact
def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()
            found = True
    if not found:
        print("No contacts found matching the search term.")

# Update a contact's details
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    print("Enter the new details (leave blank to keep current value):")
    phone = input(f"Phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
    email = input(f"Email ({contacts[name]['email']}): ") or contacts[name]['email']
    address = input(f"Address ({contacts[name]['address']}): ") or contacts[name]['address']
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print("Contact updated successfully.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# User interface
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
