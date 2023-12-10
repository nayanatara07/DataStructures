def bubble_sort(d):
    for i in range(len(d)-1):
        for j in range(len(d)-1-i):
            if d[j] > d[j+1]:
                d[j], d[j+1] = d[j+1], d[j]


d = []
size=int(input("Enter size of list:"))
for i in range (size):
        a=input()
        d.append(a)
while True:
    print("Original list:", d)
    bubble_sort(d)
    print("Sorted list:", d)
    again = input("Sort again? (y/n) ")
    if again != 'y':
        break

#NayanaTara