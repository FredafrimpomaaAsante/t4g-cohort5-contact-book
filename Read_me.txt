def add_contact(contacts):  “This line defines a function
add_contact(contacts)”

name = input(&quot;Enter name: &quot;).strip()  “the strip removes any
whitespaces”

if name in contacts:
print(f&quot;&#39;{name}&#39; already exists. Overwriting number.&quot;)

The code above checks whether the name already exits as a reserved
keyword

contacts[name] = number  “adds a new contact ”

print(f&quot;Added {name}: {number}&quot;)  confirms the contact was saved

def view_contacts(contacts):  defines a function to display all contacts

if not contacts:

print(&quot;No contacts yet.&quot;)
return

print(&quot;\n--- Contact Book ---&quot;)  prints a header and adds a blank line
for name, number in contacts.items():
print(f&quot;{name}: {number}&quot;)  prints one contact per line
print(&quot;---------------------&quot;)  “you can do away with this”

def search_contact(contacts):

query = input(&quot;Enter name to search: &quot;).strip().lower()  “reads the
search and strips whitespaces and checks for case sensitivity”

for name, number in contacts.items():
if name.lower() == query:
print(f&quot;Found: {name}: {number}&quot;)
return

print(f&quot;No contact found for &#39;{query}&#39;.&quot;)

def delete_contact(contacts):

name = input(&quot;Enter name to delete: &quot;).strip()

if name in contacts:
del contacts[name]
print(f&quot;Deleted {name}.&quot;)
else:
print(f&quot;&#39;{name}&#39; not found.&quot;)

def main():
contacts = {}  creates an empty dictionary “all the functions share
this object”

menu = &quot;&quot;&quot;  multi-line string listing options below
1. Add a contact
2. View all contacts
3. Search by name
4. Delete a contact
5. Exit
&quot;&quot;&quot;

while True:  infinite loop until you choose to exit

print(menu)  displays the menu anytime it loops

choice = input(&quot;Choose an option (1-5): &quot;).strip()  checks your
response and removes white space

if choice == &quot;1&quot;:  from here, whenever you input a number
from 1-5 it calls out the function assigned to it

add_contact(contacts)
elif choice == &quot;2&quot;:
view_contacts(contacts)
elif choice == &quot;3&quot;:
search_contact(contacts)
elif choice == &quot;4&quot;:
delete_contact(contacts)
elif choice == &quot;5&quot;:
print(&quot;Goodbye!&quot;)
break
else:
print(&quot;Invalid choice, please enter a number from 1 to 5.&quot;)  incase
the number inputted is not 1 – 5, then it prints invalid choice

if __name__ == &quot;__main__&quot;:  comparison “only true when the file is
run directly in the terminal ”

main()  starts the contact book when the program is executed