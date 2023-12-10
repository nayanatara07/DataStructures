def insertion_sort(d):
    for i in range(1, len(d)):
        x = d[i]
        j = i - 1
        while j >= 0 and x < d[j]:
            d[j+1] = d[j]
            j -= 1
        d[j+1] = x


d = []
size=int(input("Enter Size:"))
for i in range (size):
        n=input()
        d.append(n)
print("Original list:", d)
insertion_sort(d)
print("Sorted list:", d)

#NayanaTara