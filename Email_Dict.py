import pickle
import os

# File to store the dictionary
FILE_NAME = 'contacts.pkl'

# Function to load the contacts dictionary from the file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'rb') as file:
            return pickle.load(file)
    else:
        return {}

# Function to save the contacts dictionary to the file
def save_contacts(contacts):
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(contacts, file)

# Function to look up an email address
def look_up_email(contacts):
    name = input("Enter the name to look up: ")
    if name in contacts:
        print(f"{name}'s email address is {contacts[name]}")
    else:
        print(f"No entry found for {name}.")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    email = input("Enter the email address: ")
    if name in contacts:
        print(f"{name} is already in the contacts.")
    else:
        contacts[name] = email
        print(f"Contact {name} added.")

# Function to change an existing email address
def change_email(contacts):
    name = input("Enter the name to update the email address: ")
    if name in contacts:
        email = input("Enter the new email address: ")
        contacts[name] = email
        print(f"{name}'s email address has been updated.")
    else:
        print(f"No entry found for {name}.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"No entry found for {name}.")

# Function to display the menu and handle user input
def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete an existing contact")
    print("5. Exit the program")

def main():
    contacts = load_contacts()  # Load existing contacts from file
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            look_up_email(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            change_email(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)  # Save the contacts before exiting
            print("Contacts saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()