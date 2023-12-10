def binary_search(d,s):
    l = 0
    h = len(d) - 1
    while l <= h:
        m = (l + h) // 2
        if d[m] == s:
            return m
        elif d[m] < s:
            l = m + 1
        else:
            h = m - 1
    return -1

def main():
    d = []
    size=int(input("Enter size of list:"))
    for i in range (size):
        a=input()
        d.append(a)
    s = input("Enter the value to be searched: ")
    index = binary_search(d,s)
    if index == -1:
        print("Value not found")
    else:
        print("Value found at index", index)

if __name__ == '__main__':
    main()

#NayanaTara
    
