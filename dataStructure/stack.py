class stack:
    def __init__(self):
        self.stack=[]
    def __repr__(self):
        return str(self.stack)
    def __len__(self):
        return len(self.stack)
    def push(self,value):
        self.stack.append(value)
        return True
    def popElement(self):
        if len(self.stack)==0:
            print("oops nothing to pop")
            return False
        else:
            self.stack.pop()
            return True
