class Queue:
    def __init__(self):
        self.queue=[]
    def __repr__(self):
        return str(self.queue)
    def __len__(self):
        return len(self.queue)

    def add(self,value):
        if len(self.queue)==0:
            self.queue.append(value)
            return
        self.queue.insert(0,value)
    def remove(self):
        if len(self.queue)==0:
            print('oops it there is no element')
            return False
        self.queue.pop()

