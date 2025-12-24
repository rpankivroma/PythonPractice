"""
Python JSON — Task

Task Description
Write a Python program that works with JSON data to store, update, and retrieve information for a simple contact list.

Requirements

1. Create a Dictionary
Create a Python dictionary named contacts that contains at least three contacts, where each contact has:
name
email
phone
tags (a list of tags, like ["friend", "work"])

Example structure:

contacts = {
    "Alice": {"email": "alice@example.com", "phone": "12345", "tags": ["friend"]},
    "Bob":   {"email": "bob@example.com",   "phone": "67890", "tags": ["work"]},
    ...
}

2. Save to JSON
Convert the contacts dictionary to a JSON string using json.dumps()
Print this JSON string

3. Write JSON to File
Save the JSON string to a file named contacts.json
Confirm the file was written

4. Read JSON from File
Load the data back from contacts.json using json.load()
Convert it back into a Python dictionary

5. Search Contacts
Ask the user to enter a name and:
If the name exists in your contacts dictionary, print the contact details formatted nicely
If not, print:
Contact not found.

Example output:

Name: Alice
Email: alice@example.com
Phone: 12345
Tags: friend, gym

6. Add a New Contact
Ask the user to input:
Name
Email
Phone
Tags (comma-separated, e.g., friend,work)
Convert the tags input into a list
Add the new contact to the dictionary
Save the updated dictionary back to contacts.json
"""

# Answer
import json
import os

FILENAME = r"C:\Users\trade\Desktop\PythonPractice\PythonPractice\W3School\Python Tutorial\contacts.json"
# ------------------- 1. Create a Dictionary ------------------------

contacts = {
    "Alice": {"email": "alice@example.com", "phone": "12345", "tags": ["friend"]},
    "Bob":   {"email": "bob@example.com",   "phone": "67890", "tags": ["work"]},
}

# ----------------------- 2. Save to JSON ----------------------------

jeyson_contacts = json.dumps(contacts)
print("JSON string:")
print(jeyson_contacts)

# --------------------- 3. Write JSON to File ------------------------

if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)
    print("contacts.json created with default data.")

# -------------------- 4. Read JSON from File ------------------------

with open(FILENAME, "r") as file:
    contacts = json.load(file)

# --------------------- 5. Search Contacts ---------------------------

user_name = input("Enter a name: ")

if user_name in contacts:
    contact = contacts[user_name]
    print("\nContact found:")
    print("Name:", user_name)
    print("Email:", contact["email"])
    print("Phone:", contact["phone"])
    print("Tags:", ", ".join(contact["tags"]))
else:
    print("Contact not found.")

# -------------------- 6. Add a New Contact --------------------------

print("Add a New Contact")

user_name_contact = input("Enter new name: ")
user_email_contact = input("Enret new email: ")
user_phone_contact = input("Enter new phone: ")
user_tags_input = input("Tags (comma-separated): ")

user_tags = [tag.strip() for tag in user_tags_input.split(",")]

contacts[user_name_contact] = {
    "email": user_email_contact,
    "phone": user_phone_contact,
    "tags": user_tags
}

with open(FILENAME, "w") as file:
    json.dump(contacts, file, indent=4)

print("\nNew contact added and saved successfully.")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonJSON.py"
JSON string:
{"Alice": {"email": "alice@example.com", "phone": "12345", "tags": ["friend"]}, 
 "Bob": {"email": "bob@example.com", "phone": "67890", "tags": ["work"]}}
contacts.json created with default data.
Enter a name: Bob

Contact found:
Name: Bob
Email: bob@example.com
Phone: 67890
Tags: work
Add a New Contact
Enter new name: Roman
Enret new email: pankiv.roma
Enter new phone: 9567
Tags (comma-separated): my_contact,me

New contact added and saved successfully.
"""