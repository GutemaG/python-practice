def search(alist,n):
    for i in range(0,len(alist)-1):
        if(n==alist[i]):
            print("The number is found at index ",i)
            break
        else:
            continue


alist=[1,54,32,4,54,4,46,89]
search(alist,7)
