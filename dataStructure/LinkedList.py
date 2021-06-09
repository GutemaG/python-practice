class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class List():
    def __init__(self):
        self.head=None
    def insertAtFront(self,data):
        temp=self.head
        self.head=Node(data)
        self.head.next=temp
        del temp
    def listLength(self):
        temp=self.head
        length=0
        if self.isEmpty():
            return "The list is empty"
        while True:
            length+=1
            if temp.next==None:
                break
            temp=temp.next
        return length
    def insertAtEnd(self,data):
        newNode=Node(data)
        temp=self.head
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode
    def insertAtMiddel(self,data,pos):
        newNode=Node(data)
        temp1=self.head
        c=0
        if pos<0 or self.listLength()==0:
            return "Invalid Input"
        while True:
            if c==pos:
                temp2.next=newNode
                newNode.next=temp1
                break
            temp2=temp1
            temp1=temp1.next
            c+=1
    def removeFromMiddel(self,pos):
        temp1=self.head
        c=0
        while True:
            if c==pos:
                temp2.next=temp1.next
                break
            temp2=temp1
            temp1=temp1.next
            c+=1
        del temp1
    def __str__(self):
        if self.isEmpty():
            return "The list is Empty"
        currentNode=self.head
        string="The list is: "
        while currentNode is not None:
            string+=str(currentNode.data)+"  "
            currentNode=currentNode.next
        return string
    def isEmpty(self):
        return self.head is None
    def removeFront(self):
        temp=self.head
        self.head=self.head.next
        del temp
    def removeFromLast(self):
        last=self.head
        while True:
            if last.next is None:
                break
            temp=last
            last=last.next
        temp.next=None
        del last
    def printList(self):
        if self.head is None:
            print("The list is empty")
            return
        current=self.head
        while True:
            if current is None:
                break
            print(current.data)
            current=current.next

alist=List()
alist.insertAtFront(10)
alist.insertAtFront(15)
alist.insertAtFront(20)
alist.insertAtEnd(40)
alist.insertAtEnd(100)
alist.insertAtMiddel(55,2)
alist.insertAtMiddel(99,-2)
alist.insertAtEnd(33)
alist.removeFront()
#alist.removeFront()
alist.removeFromLast()
#alist.removeFromLast()
#alist.printList()
alist.removeFromMiddel(3)
alist.removeFromMiddel(1)
print(alist)
print(alist.listLength())
