def selection_sort(d):
    for i in range(len(d)-1):
        min_id = i
        for j in range(i+1, len(d)):
            if d[j] < d[min_id]:
                min_id = j
        d[i], d[min_id] = d[min_id], d[i]


d = []
size=int(input("Enter Size:"))
for i in range (size):
        a=input()
        d.append(a)
print("Original list:", d)
selection_sort(d)
print("Sorted list:", d)

#NayanaTara
