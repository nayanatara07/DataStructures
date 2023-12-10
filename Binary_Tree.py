class Node:
    def __init__(self, d):
        self.d = d
        self.lt = None
        self.rt = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, d):
        new_node = Node(d)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if d < current.d:
                    if current.lt is None:
                        current.lt = new_node
                        break
                    else:
                        current = current.lt
                else:
                    if current.rt is None:
                        current.rt = new_node
                        break
                    else:
                        current = current.rt

    def search(self, d):
        current = self.root
        while current is not None:
            if current.d == d:
                return True
            elif d < current.d:
                current = current.lt
            else:
                current = current.rt
        return False

    def delete(self, d):
        # find the node to delete
        current = self.root
        parent = None
        while current is not None and current.d != d:
            parent = current
            if d < current.d:
                current = current.lt
            else:
                current = current.rt
        if current is None:
            return False

        # case 1: the node to delete has no children
        if current.lt is None and current.rt is None:
            if parent is None:
                self.root = None
            elif parent.lt == current:
                parent.lt = None
            else:
                parent.rt = None
        # case 2: the node to delete has one child
        elif current.rt is None:
            if parent is None:
                self.root = current.lt
            elif parent.lt == current:
                parent.lt = current.lt
            else:
                parent.rt = current.lt
        elif current.lt is None:
            if parent is None:
                self.root = current.rt
            elif parent.lt == current:
                parent.lt = current.rt
            else:
                parent.rt = current.rt
        # case 3: the node to delete has two children
        else:
            successor = current.rt
            while successor.lt is not None:
                successor = successor.lt
            current.d = successor.d
            # delete the successor node
            self.delete(successor.d)

        return True
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.lt)
            print(node.d, end=' ')
            self.inorder(node.rt)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.lt)
            self.postorder(node.rt)
            print(node.d, end=' ')

    def preorder(self, node):
        if node is not None:
            print(node.d, end=' ')
            self.preorder(node.lt)
            self.preorder(node.rt)

# menu-driven interface
def main():
    tree = BinaryTree()
    while True:
        print("1. Insert a value")
        print("2. Search for a value")
        print("3. Delete a value")
        print("4. Inorder traversal")
        print("5. Postorder traversal")
        print("6. Preorder traversal")
        print("7. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = int(input("Enter the value to insert: "))
            tree.insert(value)
        elif choice ==2:
            value = int(input("Enter the value to search: "))
            if tree.search(value)==False:
                print("Element not present")
            else: 
                print("Element present")
            
        elif choice ==3:
            value = int(input("Enter the value which you want to delete: "))
            tree.delete(value)
        elif choice == 4:
            tree.inorder(tree.root)
            print()
        elif choice == 5:
            tree.postorder(tree.root)
            print()
        elif choice == 6:
            tree.preorder(tree.root)
            print()
        elif choice==7:
            break;
if __name__ == '__main__':
    main()

#NayanaTara