def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError, FileNotFoundError) as e:
            return str(e)  # Return the error message directly
    return inner

@input_error
def parse_input():
    return input("Please enter a command: ").lower().strip().split()

@input_error
def add_contact(contacts, name, number):
    contacts[name] = number
    save_contacts(contacts)
    return "Contact added."

@input_error
def change_contact(contacts, name, number):
    if name in contacts:
        contacts[name] = number
        save_contacts(contacts)
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(contacts, name):
    return contacts.get(name, "Number not found.")

@input_error
def hello():
    return 'How can I help you?'

@input_error
def show_all(contacts):
    return contacts or "Contact list is empty."

@input_error
def load_contacts():
    with open("contacts.txt", "r") as file:
        return dict(line.strip().split(":") for line in file)

@input_error
def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for name, number in contacts.items():
            file.write(f"{name}:{number}\n")

def main():
    contacts = load_contacts()
    
    while True:
        command, *args = parse_input()
        
        if command == "hello":
            print(hello())
        elif command == "add" and len(args) == 2:
            print(add_contact(contacts, *args))
        elif command == "change" and len(args) == 2:
            print(change_contact(contacts, *args))
        elif command == "phone" and len(args) == 1:
            print(show_phone(contacts, *args))
        elif command == "all" and not args:
            print(show_all(contacts))
        elif command in ("exit", "close") and not args:
            print("Goodbye!")
            break
        else:
            print('Command does not exist')

if name == "main":
    main()
