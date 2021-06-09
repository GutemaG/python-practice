class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtFront(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        #self.head.prev=None
    def __str__(self):
        string=[]
        temp=self.head        
        while True:
            if temp is None:
                break
            string.append(temp.data)
            temp=temp.next
        del temp
        return str(string)
    def insertAtEnd(self,data):
        newNode=Node(data)
        temp=self.head
        temp2=None
        while temp is not None:
            temp2=temp
            temp=temp.next
        temp2.next=newNode
        newNode.next=temp
        del temp
        del temp2
    def insertAtMiddel(self,data,pos):
        newNode=Node(data)
        temp=self.head
        temp2=None
        co=0
        while(co<pos):
            temp2=temp
            temp=temp.next
            co+=1
        temp2.next=newNode
        newNode.next=temp
        del temp
        del temp2
    def deleteFront(self):
        temp=self.head
        self.head=self.head.next
        del temp
    def deleteEnd(self):
        temp=self.head
        temp2=None
        while temp.next is not None:
            temp2=temp
            temp=temp.next

        temp2.next=None
        del temp2
        del temp
    def deleteAtMiddel(self,pos):
        temp=self.head
        temp2=None
        counter=0
        while counter<pos:
            temp2=temp
            temp=temp.next
            counter+=1
        temp2.next=temp.next
        temp.next.prev=temp2
        del temp
        del temp2



alist=LinkedList()
alist.insertAtFront(20)
alist.insertAtFront(30)
alist.insertAtFront(15)
alist.insertAtEnd(100)
alist.insertAtEnd(200)
alist.insertAtEnd(300)
alist.insertAtMiddel(333,3)
alist.insertAtMiddel(222,2)
alist.deleteEnd()
alist.deleteAtMiddel(2)
#alist.deleteFront()
#alist.deleteFront()
alist.deleteAtMiddel(3)
alist.deleteEnd()
print(alist)
