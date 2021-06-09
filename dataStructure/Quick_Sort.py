def quickSort(alist, leftEnd, rightEnd):
    left = leftEnd
    right = rightEnd
    pivotPoint = (leftEnd+rightEnd)/2
    pivot = alist[pivotPoint]
    while(left < right):
        while(alist[left] < pivot):
            left += 1
        while(alist[right] > pivot):
            right -= 1
        if(left <= right):
            alist[left], alist[right] = alist[right], alist[left]
            left += 1
            right -= 1
    if(leftEnd < right):
        quickSort(alist, leftEnd, right)
    if(left < rightEnd):
        quickSort(alist, left, rightEnd)


alist = [10, 15, 56, 13, 66, 8, 4, 21, 45, 53, 12, 2, 77, 5]
quickSort(alist, 0, len(alist)-1)
print(alist)
