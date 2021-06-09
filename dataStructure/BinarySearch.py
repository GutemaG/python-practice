def binarysearch(alist,value):
    if len(alist)==0 or (len(alist)==1 and alist[0]!=value):return False
    mid=alist[int(len(alist)/2)]
    if value==mid:return True
    if value<mid:
        return binarysearch(alist[:int(len(alist)/2)],value)
    if value>mid:
        return binarysearch(alist[int(len(alist)/2):],value)

#alist=[1,2,3,5,6,7,8,9]
#binarysearch(alist,49)
