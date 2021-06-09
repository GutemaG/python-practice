class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
    def getData(self):
        return self.data
    def setData(self,data):
        self.data=data
    def getNextNode(self):
        return self.nextNode
    def setNextNode(self,newNode):
        self.nextNode=newNode


class List:
    def __init__(self):
        self.firstNode=None
        self.lastNOde=None
    def __str__(self):
        if self.isEmpty():
            return "The List is empty"
        currentNode=self.firstNode
        string="The List is: "
        while currentNode is not None:
            string+=str(currentNode.getData())+ " "
            currentNode=currentNode.getNextNode()
        return string
    def insertAtFront(self,value):
        newNode=Node(value)
        if self.isEmpty():
            self.firstNode=self.lastNode=newNode
        else:
            newNode.setNextNode(self.firstNode)
            self.firstNode=newNode
    def removeFromFront(self):
        if self.isEmpty():
           raise IndexError("Empty elements")
        if self.firstNode is self.lastNode:
           self.firstNode=self.lastNode=None
        else:
            self.firstNode=self.firstNode.getNextNode()
        return True
    def removeFromLast(self):
        if self.isEmpty():
            raise IndexError("List is empty")
        if self.firstNode is self.lastNode:
            self.firstNode=self.lastNode=None
        else:
            currentNode=self.firstNode
            while currentNode.getNextNode() is not self.lastNode:
                currentNode=currentNode.getNextNode()
            currentNode.setNextNode(None)
            self.lastNode=currentNode
        return True
    def insertAtMiddel(self,value,pos):
        newNode=Node(value)
        temp1=self.firstNode
        temp2=None
        counter=0
        while True:
            if pos==counter:
                temp2.setNextNode(newNode)
                newNode.setNextNode(temp1)
                break
            temp2=temp1
            temp1.getNextNode()
            counter+=1
        '''while counter<pos:
            temp2=temp1
            temp1.getNextNode()
            counter+=1
        temp2.setNextNode(newNode)
        newNode.setNextNode(temp2.getNextNode().getNextNode())
        temp2.setNextNode(newNode)
        temp1.setNextNode(temp2.getNextNode())'''
        return True

    def isEmpty(self):
        return self.firstNode is None

import sys
#from list import list
'''def instruction():
    print("Enter 1 for insert at the beginning ", "5 for exit")
listObject=List()
instruction()
ch=input("?")
while ch!=5:
    if ch=="1":
        listObject.insertAtFront(input("Enter value "))
       # print(listObject)
    elif ch=="9":
        listObject.removeFromFront()
    elif ch=="5":
        print("Bye")
        print(listObject)
        break
    elif ch=="m":
        listObject.insertAtMiddel(input("value"),int(input("Position")))
    elif ch=="r":
        listObject.removeFromLast()
    else:
        print("Wrong input")
    ch=input("?")
'''
listObject=List()
listObject.insertAtFront(5)
listObject.insertAtFront(4)
listObject.insertAtFront(3)
listObject.insertAtFront(2)
listObject.insertAtFront(1)
listObject.insertAtFront(0)
listObject.insertAtMiddel(9,3)
print(listObject)
