class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None
    def printLinkedList(self):
        printval=self.head
        if printval.next==None:
            print("oops i am empty")
        while printval is not None:
            print(printval.data,end=" -> ")
            printval=printval.next
        print('\n')
    def insertAtBegin(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
    def insertAtEnd(self,value):
        printval=self.head
        while printval.next is not None:
            printval=printval.next
        newNode=Node(value)
        printval.next=newNode
        newNode.next=None
        
    def insertAt(self,value,index):
        current=self.head
        newNode=Node(value)
        for i in range(0,index):
            current=current.next
        current.next=newNode
        newNode.next=current.next.next
        current=None
    def removeAtBegin(self):
        h=self.head
        self.head=self.head.next
        h=None
    def removeAtEnd(self):
        removedval=self.head
        while removedval.next is not None:
            removedval=removedval.next
        removedval=None



list1=SLinkedList()
list1.head=Node('Mon')
e2=Node('Tue')
e3=Node('wed')

list1.head.next=e2
e2.next=e3
list1.insertAtBegin("sun")
