# List As Queue

from collections import deque
queue = deque()
while True:
    action = input("Enqueue, Dequeue, or Quit: ").lower()
    if action == "enqueue":
        item = input("Enter item: ")
        queue.append(item)
        print("Queue:", list(queue))
    elif action == "dequeue":
        if queue:
            dequeued = queue.popleft()
            print("Dequeued:", dequeued)
            print("Queue:", list(queue))
        else:
            print("Queue empty")
    elif action == "quit":
        break