class Node:
    def __init__(self, d=None, n=None):
        self.d = d
        self.n = n


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, d):
        # Insert a new node at the beginning of the list
        new_node = Node(d, self.head)
        self.head = new_node

    def insert_at_end(self, d):
        # Insert a new node at the end of the list
        new_node = Node(d)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.n:
            current = current.n
        current.n = new_node

    def delete_node(self, d):
        # Delete the first node with the given data
        if self.head is None:
            return
        if self.head.d == d:
            self.head = self.head.n
            return
        current = self.head
        while current.n:
            if current.n.d == d:
                current.n = current.n.n
                return
            current = current.n

    def find_node(self, d):
        # Find the first node with the given data and return it, or return None if not found
        current = self.head
        while current:
            if current.d == d:
                return current
            current = current.n
        return None

    def print_list(self):
        # Print the data in each node of the list
        current = self.head
        while current:
            print(current.d)
            current = current.n


def print_menu():
    print('1. Insert at front')
    print('2. Insert at end')
    print('3. Delete node')
    print('4. Find node')
    print('5. Print list')
    print('6. Quit')
    print()


linked_list = LinkedList()

while True:
    print_menu()
    choice = int(input('Enter your choice: '))

    if choice == 1:
        d = input('Enter data to insert: ')
        linked_list.insert_at_front(d)
    elif choice == 2:
        d = input('Enter data to insert: ')
        linked_list.insert_at_end(d)
    elif choice == 3:
        d = input('Enter data to delete: ')
        linked_list.delete_node(d)
    elif choice == 4:
        d = input('Enter data to find: ')
        n = linked_list.find_node(d)
        if node:
            print('Node found:', node.d)
        else:
            print('Node not found')
    elif choice == 5:
        linked_list.print_list()
    elif choice == 6:
        break
    else:
        print('Invalid choice. Enter a number between 1 and 6.')
    print()

#NayanaTara

    
