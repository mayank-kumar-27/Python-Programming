# Dict Practical Uses

contacts = {}
while True:
    action = input("Add, Search, Show, or Quit: ").lower()
    if action == "add":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
    elif action == "search":
        name = input("Enter name: ")
        print("Phone:", contacts.get(name, "Not found"))
    elif action == "show":
        if contacts:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")
    elif action == "quit":
        break