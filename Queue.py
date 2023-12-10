class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.its = []

    def enqueue(self, it):
        # Add an item to the end of the queue
        self.its.append(it)

    def dequeue(self):
        # Remove and return the item at the front of the queue
        return self.its.pop(0)

    def peek(self):
        # Return the item at the front of the queue without removing it
        return self.its[0]

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return not self.its
    def display(self):
        # Print the items in the stack
        for it in self.its:
            print(it)


def print_menu():
    print('1. Enqueue an item')
    print('2. Dequeue an item')
    print('3. Peek at the front item')
    print('4. Check if the queue is empty')
    print('5. Quit')
    print()


queue = Queue()

while True:
    print_menu()
    choice = int(input('Enter your choice: '))

    if choice == 1:
        it = input('Enter an item to enqueue: ')
        queue.enqueue(it)
    elif choice == 2:
        if queue.is_empty():
            print('The queue is empty.')
        else:
            print('Dequeued', queue.dequeue())
    elif choice == 3:
        if queue.is_empty():
            print('The queue is empty.')
        else:
            print('Peeked', queue.peek())
    elif choice == 4:
        if queue.is_empty():
            print('The queue is empty.')
        else:
            print('The queue is not empty.')
    elif choice == 5:
        break
    elif choice==6:
        print(queue.display())
    else:
        print('Invalid choice. Enter a number between 1 and 5.')
    print()

#NayanaTara
