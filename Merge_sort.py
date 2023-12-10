def merge(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            list[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            list[k]=right[j]
            j=j+1
            k=k+1

list=[]
size=int(input("Enter size of list"))
for i in range (size):
        a=input()
        list.append(a)
print("before sorting:",list)
merge(list)
print("After sorting ",list)

#NayanaTara
