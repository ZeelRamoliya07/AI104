"""
Write a Python program to create a class representing a queue data structure. Include methods
for enqueueing and dequeuing elements.
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue.")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
            return None
        removed_item = self.queue.pop(0)
        print(f"{removed_item} removed from the queue.")

    def display(self):
        if not self.queue:
            print("Queue is empty.")
            return
        print("Queue:", " <- ".join(map(str, self.queue)))

def queue_menu():
    q = Queue()
    
    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter value to enqueue: ")
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Try again.")

queue_menu()
