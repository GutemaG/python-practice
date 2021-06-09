def insertionsort(array):
    for i in range(1,len(array)):
        temp=array[i]
        j=i-1
        while j>=0 and array[j]>temp:
            array[j+1]=array[j]
            j=j-1
    
        array[j+1]=temp
        

array=[5,4,2,10,1,45,6,41,21,13,34,78,0,3]
insertionsort(array)
print(array)
