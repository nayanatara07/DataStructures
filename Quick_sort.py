def quick_sort(arr):
    if len(arr) < 2:
        return arr
    piv = arr[0]
    a = [i for i in arr[1:] if i <= piv]
    b = [i for i in arr[1:] if i > piv]
    return quick_sort(a) + [piv] + quick_sort(b)
d = []
size=int(input("Enter Size:"))
for i in range (size):
        n=input()
        d.append(n)
res = quick_sort(d)
print(res)  

#NayanaTara
