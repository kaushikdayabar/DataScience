class Queue:

    def __init__(self):
        self.Queue1=[]
    
    def enQueue(self,data):
        self.Queue1.insert(0,data)
        print(self.Queue1)
    
    def deQueue(self):
        self.Queue1.pop()
        print(self.Queue1)
    
    def size(self):
        return len(self.Queue1)
    
    def isEmpty(self):
        return len(self.Queue1)==0


ob=Queue()

print("Enqueue 1 , 2 and 3 ")
ob.enQueue(1)
ob.enQueue(2)
ob.enQueue(3)

print("Dequeue last 2 ")
ob.deQueue()
ob.deQueue()

print("Size of Queue")
print(ob.size())

print("Is Empty ")
print(ob.isEmpty())

print("dequeue last 1")
ob.deQueue()

print("Size of Queue")
print(ob.size())

print("Is Empty ")
print(ob.isEmpty())

