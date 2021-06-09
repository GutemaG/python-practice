class Stack:
    def __init__(self):
        self.stack=[]
    def __str__(self):
        return str(self.stack)
    def Push(self,value):
        self.stack.append(value)
        return True
    def Pop(self):
        if len(self.stack)==0:
            return "The Stack is Empty"
        else:
            self.stack.pop()
            return True
    def peek(self):
        return self.stack[len(self.stack)-1]


stack=Stack()
stack.Push(10)
stack.Push(20)
stack.Push(40)
#stack.Push(100)
stack.Pop()
print(stack)
