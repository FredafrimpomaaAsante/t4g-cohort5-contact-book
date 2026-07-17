def add_contact(contacts): --> “This line defines a function
(add_contact(contacts))”

name = input("Enter name: ").strip() --> “the strip removes any
whitespaces”

if name in contacts:
print(f"'{name}' already exists. Overwriting number.")

The code above checks whether the name already exits as a reserved
keyword

contacts[name] = number  “adds a new contact ”

print(f"Added {name}: {number}")  confirms the contact was saved

def view_contacts(contacts):  defines a function to display all contacts

if not contacts:

print("No contacts yet.")
return

print("\n--- Contact Book ---")  prints a header and adds a blank line
for name, number in contacts.items():
print(f"{name}: {number}")  prints one contact per line
print("---------------------") --> “you can do away with this”

def search_contact(contacts):

query = input("Enter name to search: ").strip().lower() --> “reads the
search and strips whitespaces and checks for case sensitivity”

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
contacts = {} --> creates an empty dictionary “all the functions share
this object”

menu = """ --> multi-line string listing options below
1. Add a contact
2. View all contacts
3. Search by name
4. Delete a contact
5. Exit
"""

while True: --> infinite loop until you choose to exit

print(menu) --> displays the menu anytime it loops

choice = input("Choose an option (1-5): ").strip() --> checks your
response and removes white space

if choice == "1": --> from here, whenever you input a number
from 1-5 it calls out the function assigned to it

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
print("Invalid choice, please enter a number from 1 to 5.") --> incase
the number inputted is not 1 – 5, then it prints invalid choice

if __name__ == "__main__": --> comparison “only true when the file is
run directly in the terminal ”

main() --> starts the contact book when the program is executed