# List As Stack

stack = []
while True:
    action = input("Push, Pop, or Quit: ").lower()
    if action == "push":
        item = input("Enter item: ")
        stack.append(item)
        print("Stack:", stack)
    elif action == "pop":
        if stack:
            popped = stack.pop()
            print("Popped:", popped)
            print("Stack:", stack)
        else:
            print("Stack empty")
    elif action == "quit":
        break