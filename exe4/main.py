from pathlib import Path
import json

def parse_input(user_input):
    cmd, *args = user_input.split(maxsplit=1)
    cmd = cmd.strip().lower()
    if args:
        args = args[0].split()
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command. Usage: add <name> <phone>"
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    contacts[name] = phone
    save_contacts(contacts)  # Save contacts to dict.json after adding
    return "Contact added."

def show_phone(name, contacts):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def show_all(contacts):
    print("All saved contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def change_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command. Usage: change <name> <new_phone>"

    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        save_contacts(contacts)  # Save contacts to dict.json after changing
        return f"Contact updated for {name}."
    else:
        return f"Contact {name} not found."

def main():
    contacts = load_contacts()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Saving contacts...")
            save_contacts(contacts)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "all":
            show_all(contacts)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command.startswith("phone "):
            name = command.split(maxsplit=1)[1].strip()
            show_phone(name, contacts)
        else:
            print("Invalid command.")

def load_contacts():
    contacts = {}
    file_path = 'dict.json'
    if Path(file_path).is_file():
        with open(file_path, 'r', encoding='utf-8') as f:
            contacts = json.load(f)
    return contacts

def save_contacts(contacts):
    with open('dict.json', 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
