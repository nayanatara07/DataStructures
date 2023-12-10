class Node:
    def __init__(self, d=None, p=None, n=None):
        self.d = d
        self.p = p
        self.n = n

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, d):
        new_node = Node(d, None, None)
        if self.head is None:
            self.head = new_node
            new_node.p = self.head
            new_node.n = self.head
        else:
            current_node = self.head
            while current_node.n != self.head:
                current_node = current_node.n
            current_node.n = new_node
            new_node.p = current_node
            new_node.n = self.head
            self.head.p = new_node

    def prepend(self, d):
        new_node = Node(d, None, None)
        if self.head is None:
            self.head = new_node
            new_node.p = self.head
            new_node.n = self.head
        else:
            current_node = self.head
            while current_node.n != self.head:
                current_node = current_node.n
            current_node.n = new_node
            new_node.p = current_node
            new_node.n = self.head
            self.head.p = new_node
            self.head = new_node

    def delete(self, d):
        if self.head is None:
            return
        if self.head.d == d:
            current_node = self.head
            while current_node.n != self.head:
                current_node = current_node.n
            if self.head == self.head.n:
                self.head = None
            else:
                current_node.n = self.head.n
                self.head.n.p = current_node
                self.head = self.head.n
        else:
            current_node = self.head
            while current_node.n != self.head:
                if current_node.n.d == d:
                    current_node.n = current_node.n.n
                    current_node.n.p = current_node
                    break
                current_node = current_node.n

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.d)
            current_node = current_node.n
            if current_node == self.head:
                break
        print(elements)

cdl_list = CircularDoubleLinkedList()

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
        cdl_list.append(d)
    elif choice == 2:
        d = input("Enter the element to prepend: ")
        cdl_list.prepend(d)
    elif choice == 3:
        d = input("Enter the element to delete: ")
        cdl_list.delete(d)
    elif choice == 4:
        cdl_list.display()
    elif choice == 5:
        break

#NayanaTara
