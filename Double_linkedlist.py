class Node:
    def __init__(self, d=None, p=None, n=None):
        self.d = d
        self.p = p
        self.n = n

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, d):
        new_node = Node(d, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.p = self.tail
            new_node.n = None
            self.tail.n = new_node
            self.tail = new_node

    def prepend(self, d):
        new_node = Node(d, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.p = new_node
            self.head = new_node

    def delete(self, d):
        current_node = self.head
        while current_node is not None:
            if current_node.d == d:
                if current_node.p is not None:
                    current_node.p.n = current_node.n
                    current_node.n.p = current_n.p
                else:
                    self.head = current_node.n
                    current_node.n.p = None
                break
            current_node = current_node.n

    def display(self):
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(current_node.d)
            current_node = current_node.n
        print(elements)

dl_list = DoubleLinkedList()

while True:
    print("Menu:")
    print("1. Append an element")
    print("2. Prepend an element")
    print("3. Delete an element")
    print("4. Display the list")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        d = input("Enter the element to append: ")
        dl_list.append(d)
    elif choice == 2:
        d = input("Enter the element to prepend: ")
        dl_list.prepend(d)
    elif choice == 3:
        d = input("Enter the element to delete: ")
        dl_list.delete(d)
    elif choice == 4:
        dl_list.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

#NayanaTara
