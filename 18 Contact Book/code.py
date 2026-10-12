# Define a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact(name, email, phone):
    contacts[name] = {'email': email, 'phone': phone}
    print(f"Added contact: {name}")

# Function to edit an existing contact
def edit_contact(name, email=None, phone=None):
    if name in contacts:
        if email:
            contacts[name]['email'] = email
        if phone:
            contacts[name]['phone'] = phone
        print(f"Updated contact: {name}")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted contact: {name}")
    else:
        print("Contact not found.")

# Function to view contact details
def view_contact(name):
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}, Email: {contact['email']}, Phone: {contact['phone']}")
    else:
        print("Contact not found.")

# Example Usage
add_contact("Cliff Lolita", "cliff@example.com", "123-456-7890")
edit_contact("Cliff Lolita", email="cliff.lolita@example.com")
view_contact("Cliff Lolita")
delete_contact("Cliff Lolita") 
