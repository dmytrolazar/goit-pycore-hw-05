def input_error_add_contact(func):
    def inner(*args, **kwargs):
        if len(args[0]) != 2:
            return "Enter name and phone to add a contact."
        return func(*args, **kwargs)
    return inner

def input_error_change_contact(func):
    def inner(*args, **kwargs):
        if len(args[0]) != 2:
            return "Enter name and phone to change a contact."
        return func(*args, **kwargs)
    return inner

def input_error_show_contact(func):
    def inner(*args, **kwargs):
        try:
            if len(args[0]) != 1:
                return "Enter a name of a contact to show."
            return func(*args, **kwargs)
        except KeyError:
            return "Contact doesn't exist."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error_add_contact
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already exists."

@input_error_change_contact
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact doesn't exist."

@input_error_show_contact
def show_contact(args, contacts):
    return f"{contacts[args[0]]}"

def show_all_contacts(contacts):
    result = ''
    for name, phone in contacts.items():
        result += f"{name}: {phone}\r\n"
    return f"{result.strip()}" if result != '' else "Your contact list is empty."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"] and len(args) == 0:
            print("Good bye!")
            break
        elif command == "hello" and len(args) == 0:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all" and len(args) == 0:
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()