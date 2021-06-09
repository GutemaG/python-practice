class queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        return str(self.queue)
    def insert(self,value):
        if len(self.queue)==0:#if value not in self.queue
            self.queue.append(value)
        else:
            self.queue.insert(0,value)
            return True
    def remove(self):
        if len(self.queue)==0:
            return "The list is Empty"
        else:
            self.queue.pop()


qu=queue()
qu.insert(20)
qu.insert(15)
qu.insert(3)
qu.insert(30)
qu.insert(55)
qu.remove()
print(qu)
