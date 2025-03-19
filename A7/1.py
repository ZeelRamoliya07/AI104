"""
Write a Python program to create a class representing a linked list data structure. Include
methods for displaying linked list data, inserting and deleting nodes.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            print("Key not found!")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        if not temp:
            print("Linked List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Menu-driven program
def linked_list_menu():
    linked_list = LinkedList()
    
    while True:
        print("\n1. Insert at End")
        print("2. Delete Node")
        print("3. Display Linked List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter value to insert: ")
            linked_list.insert_at_end(data)
        elif choice == '2':
            key = input("Enter value to delete: ")
            linked_list.delete_node(key)
        elif choice == '3':
            linked_list.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Try again.")

linked_list_menu()
