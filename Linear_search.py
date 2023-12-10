def linear_search(d,s):
    for i in range(len(d)):
        if d[i] == s:
            print("The number to be searched is found at:",i)
    

def main():
    d = []
    limit=int(input("Enter size of list:"))
    for i in range (limit):
        n=input()
        d.append(n)
    s = input("Enter the searching value: ")
    index = linear_search(d,s)
        

if __name__ == '__main__':
    main()

# Here,d=data and s=the value to be searched
#NayanaTara
