def add_contact(contacts):
    name = input("Enter name: ").strip()
    number = input("Enter number: ").strip()

    if name in contacts:
        print(f"'{name}' already exists. Overwriting number.")

    contacts[name] = number
    print(f"Added {name}: {number}")


def view_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return

    print("\n--- Contact Book ---")
    for name, number in contacts.items():
        print(f"{name}: {number}")
    


def search_contact(contacts):
    
    query = input("Enter name to search: ").strip().lower()

    for name, number in contacts.items():
        if name.lower() == query:
            print(f"Found: {name}: {number}")
            return

    print(f"No contact found for '{query}'.")


def delete_contact(contacts):
    
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}.")
    else:
        print(f"'{name}' not found.")


def main():
    contacts = {}

    menu = """
1. Add a contact
2. View all contacts
3. Search by name
4. Delete a contact
5. Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()